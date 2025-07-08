import cv2
import os

def capture_images(name, roll_no, img_count=20):
    folder_name = f"{roll_no}_{name}"
    save_path = os.path.join("dataset", folder_name)
    os.makedirs(save_path, exist_ok=True)

    cam = cv2.VideoCapture(0)
    print(f"\n📸 Capturing {img_count} images for {name} ({roll_no})...")

    count = 0
    while count < img_count:
        ret, frame = cam.read()
        if not ret:
            break

        cv2.imshow("Capture - Press Esc to stop", frame)
        img_name = os.path.join(save_path, f"{name}_{count+1}.jpg")
        cv2.imwrite(img_name, frame)
        count += 1
        print(f"✅ Captured image {count}/{img_count}")

        if cv2.waitKey(100) & 0xFF == 27:  # Press Esc to exit early
            print("⏹️ Capture stopped by user.")
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"\n✅ All images saved in: {save_path}")

if __name__ == "__main__":
    name = input("Enter name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    try:
        img_count = int(input("Enter number of images to capture (default 20): ") or 20)
    except ValueError:
        img_count = 20

    capture_images(name, roll_no, img_count)
