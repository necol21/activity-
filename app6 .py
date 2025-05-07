import streamlit as st
import cv2
import numpy as np

st.title("Real-Time Webcam Capture with OpenCV")

# Start the webcam only when button is clicked
run = st.checkbox('Start Webcam')

FRAME_WINDOW = st.image([])

# Initialize video capture
camera = cv2.VideoCapture(0)

if run:
    while True:
        # Read frame from webcam
        ret, frame = camera.read()
        if not ret:
            st.error("Failed to grab frame")
            break

        # Convert from BGR (OpenCV default) to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Show frame in Streamlit
        FRAME_WINDOW.image(frame)

else:
    st.write("Webcam stopped.")

# Release the camera when done (Streamlit auto-exits loop on stop)
camera.release()
