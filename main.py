import csv
import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Load the cascade
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load images and labels
face_images_dir = 'images'
known_face_encodings = []
known_face_names = []
for root, dirs, files in os.walk(face_images_dir):
    for file in files:
        if file.endswith("jpg") or file.endswith("png"):
            known_face_names.append(os.path.splitext(file)[0])
            face_image = face_recognition.load_image_file(os.path.join(root, file))
            face_encoding = face_recognition.face_encodings(face_image)[0]
            known_face_encodings.append(face_encoding)

# Function to mark attendance
def mark_attendance(name):
    with open('attendance.csv', 'a', newline='') as file:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        writer = csv.writer(file)
        writer.writerow([name, dt_string])

# List to keep track of marked persons
marked_persons = []

# Tkinter GUI
root = tk.Tk()
root.title("Smile Detection and Attendance Marking")

# Create a label
label = tk.Label(root, text="Smile Detection and Attendance Marking", font=("Arial", 16))
label.pack(pady=10)

# Create a canvas
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# To capture video from webcam.
video = cv2.VideoCapture(0)

# Function to update the video feed
def update_feed():
    ret, frame = video.read()
    if ret:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare face encodings with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            faceDis = face_recognition.face_distance(known_face_encodings, face_encoding)
            matchIndex = np.argmin(faceDis)
            name = "Unknown"
            if matches[matchIndex]:
                name = known_face_names[matchIndex].upper()

            # Draw the rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 3)

            # Display the name
            cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            # Detect the smile within the face region
            roi_gray = frame[top:bottom, left:right]
            smile = smile_cascade.detectMultiScale(cv2.cvtColor(roi_gray, cv2.COLOR_BGR2GRAY), scaleFactor=1.8, minNeighbors=20)
            if len(smile) > 0 and name not in marked_persons:
                marked_persons.append(name)
                mark_attendance(name)

            for (x, y, w, h) in smile:
                cv2.putText(frame, 'SMILING', (left+x, top+y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        canvas.img = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.after(10, update_feed)

# Function to close the application
def close_app():
    video.release()
    root.destroy()

# Button to close the application
close_button = tk.Button(root, text="Close", command=close_app, font=("Arial", 12), bg="red", fg="white")
close_button.pack(pady=10)

# Run the update feed function
update_feed()

# Run the Tkinter main loop
root.mainloop()
