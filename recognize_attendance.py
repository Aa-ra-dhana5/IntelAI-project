import cv2
import face_recognition
import pickle
import datetime
import os

def recognize_and_log():
    # Load known face encodings
    data = pickle.load(open("encodings.pickle", "rb"))
    known_encodings = data["encodings"]
    known_names = data["names"]

    # Initialize webcam
    cam = cv2.VideoCapture(0)
    today = datetime.date.today().strftime("%Y-%m-%d")
    log_file = f"attendance/{today}.csv"
    seen = set()

    # Create attendance folder and today's log file if not exists
    os.makedirs("attendance", exist_ok=True)
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("Name,Time\n")

    frame_count = 0
    max_frames = 300  # Automatically stop after ~10 seconds at 30 FPS

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding, box in zip(encodings, boxes):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                matched_idx = matches.index(True)
                name = known_names[matched_idx]

                if name not in seen:
                    time_str = datetime.datetime.now().strftime("%H:%M:%S")
                    with open(log_file, "a") as f:
                        f.write(f"{name},{time_str}\n")
                    seen.add(name)

            top, right, bottom, left = box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        cv2.imshow("Attendance System - Press ESC to stop", frame)
        if cv2.waitKey(1) == 27 or frame_count > max_frames:
            break

        frame_count += 1

    cam.release()
    cv2.destroyAllWindows()

# DO NOT call recognize_and_log() directly when imported by Streamlit
