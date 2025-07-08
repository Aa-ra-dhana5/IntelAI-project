import face_recognition
import pickle
import os

def encode_faces():
    encodings = []
    names = []

    for root, dirs, files in os.walk("dataset"):
        for file in files:
            if file.endswith(".jpg"):
                path = os.path.join(root, file)
                name = os.path.basename(root)
                image = face_recognition.load_image_file(path)
                face_enc = face_recognition.face_encodings(image)
                if face_enc:
                    encodings.append(face_enc[0])
                    names.append(name)

    data = {"encodings": encodings, "names": names}
    with open("encodings.pickle", "wb") as f:
        pickle.dump(data, f)

    print("[INFO] Face encoding completed.")

encode_faces()