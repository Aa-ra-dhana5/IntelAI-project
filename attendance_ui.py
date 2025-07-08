import streamlit as st
import os
import pandas as pd
from capture_images import capture_images
from encode_faces import encode_faces
from recognize_attendance import recognize_and_log

st.set_page_config(page_title="AI Attendance System", layout="centered")
st.title("🧠 AI-Powered Face Attendance System")

os.makedirs("dataset", exist_ok=True)
os.makedirs("attendance", exist_ok=True)

menu = st.sidebar.radio("Select Action", [
    "Register New User",
    "Take Attendance",
    "View Attendance Logs"
])

# Register new face
if menu == "Register New User":
    st.subheader("📸 Register New Face")
    name = st.text_input("Enter Full Name")
    roll = st.text_input("Enter Roll Number")
    count = st.slider("Number of Images to Capture", 1, 5, 10)

    if st.button("Capture Images and Encode"):
        if not name or not roll:
            st.warning("Please enter both name and roll number.")
        else:
            capture_images(name, roll, count)
            encode_faces()
            st.success(f"{name} registered and encoded successfully.")

# Take attendance
elif menu == "Take Attendance":
    st.subheader("📷 Take Attendance via Webcam")

    if st.button("Start Attendance"):
        st.info("📡 Starting webcam. Press ESC in the webcam window to stop.")
        try:
            recognize_and_log()
            st.success("✅ Attendance recorded successfully.")
        except Exception as e:
            st.error(f"❌ Error occurred: {e}")


# View logs
elif menu == "View Attendance Logs":
    st.subheader("📁 Attendance Logs")
    logs = sorted([f for f in os.listdir("attendance") if f.endswith(".csv")])

    if not logs:
        st.info("No attendance logs found.")
    else:
        selected_log = st.selectbox("Select Date", logs)
        if selected_log:
            df = pd.read_csv(os.path.join("attendance", selected_log))
            st.dataframe(df)

            st.download_button(
                label="📥 Download CSV",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name=selected_log,
                mime="text/csv"
            )
