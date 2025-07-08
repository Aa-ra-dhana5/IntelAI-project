# 🧑‍🏫 Face Recognition Attendance System

A Python-based real-time face recognition attendance system using OpenCV and the `face_recognition` library. It allows you to register individuals by capturing face images, encode their facial features, and then automatically recognize them via webcam for attendance tracking.

---

## 📌 Features

- Capture face images with name and roll number
- Encode and store facial data
- Real-time face recognition using webcam
- Auto-mark attendance for recognized individuals
- Organized dataset folder structure

---

## 🛠 Tech Stack

- Python 3.10
- OpenCV
- face_recognition (built on dlib)
- Numpy
- CSV (for attendance records)

---

## 🚀 How It Works

1. **Capture Images**:
   Run the script to capture images of a student:
   ```bash
   python capture_images.py
   ````

This will save 20 images per person into `dataset/{roll_no}_{name}`.

2. **Encode Faces:**
   Generate facial encodings from the saved images:

   ```bash
   python encode_faces.py
   ```

   This will create `encodings.pickle`.

3. **Run Attendance System:**
   Start the live webcam-based attendance system:

   ```bash
   python recognize_attendance.py
   ```

4. Attendance will be saved to a CSV file with date & time.

---

## 📂 Project Structure

```
FaceAttendanceSystem/
│
├── dataset/                         # Folder with subfolders of face images
│   └── 002_Aksharaa/      # Example
│       ├── Aksharaa_1.jpg
│       └── ...
│
├── capture_images.py               # Script to capture face images
├── encode_faces.py                 # Encode known faces into pickle file
├── recognize_attendance.py  # Main attendance script
├── encodings.pickle                # Saved face encodings
└── README.md
```

---

## ⚠️ Troubleshooting

### Installing `face_recognition` and `dlib` on Windows:

1. Download compatible `.whl` files from:

   * [https://github.com/z-mahmud22/Dlib\_Windows\_Python3.x](https://github.com/z-mahmud22/Dlib_Windows_Python3.x)
   * [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#face-recognition](https://www.lfd.uci.edu/~gohlke/pythonlibs/#face-recognition)

2. Install manually using PowerShell:

   ```bash
   pip install path_to_downloaded_whl_file.whl
   ```

Example:

```bash
pip install dlib-19.24.2-cp310-cp310-win_amd64.whl
pip install face_recognition-1.3.0-py310-win_amd64.whl
```

---

## ✅ To-Do

* [ ] Integrate with Google Sheets or Excel
* [ ] Add GUI using Tkinter or PyQt
* [ ] Deploy on Raspberry Pi

---

## 🤝 Contributing

Pull requests are welcome. Feel free to fork and enhance the system with new features!

---

## 📜 License

This project is for educational purposes only.

---


