# Attendance-System-Using-Face-Recognition
 ## Project Overview

The Attendance System Using Face Recognition is a smart and automated solution designed to record attendance using facial recognition technology. This system eliminates manual attendance, reduces proxy entries, and improves accuracy by identifying individuals through their facial features in real time.

The project is developed using Python and integrates Computer Vision, Artificial Intelligence, and Database Management concepts to create a reliable and user-friendly attendance system.


🎯 Objectives

To automate the attendance process using face recognition

To prevent proxy attendance

To store attendance records securely

To provide an easy way to view attendance data

To implement a contactless and efficient system


🧠 Technologies & Libraries Used

Programming Language

Python – Core language used to develop the system


Libraries

OpenCV (cv2) – Captures real-time video and processes images

face_recognition – Detects and recognizes faces using deep learning

MediaPipe – Performs face landmark detection for blink (liveness) detection

NumPy – Handles numerical and array operations

SQLite3 – Stores attendance records locally in a database

Tkinter – Provides a simple GUI to view attendance

OS Module – Executes Python files and handles file operations

Datetime – Records date and time of attendance



---

🧩 Project Structure

Attendance-System-Using-Face-Recognition/
│
├── app.py                 # Main menu (Start system / View attendance)
├── main.py                # Face recognition & attendance marking logic
├── view_attendance.py     # GUI to display attendance records
├── attendance.db          # SQLite database (auto-created)
├── dipendra.jpg           # Sample student image
├── README.md              # Project documentation


⚙️ How the System Works

1️⃣ App Menu (app.py)

Displays two options:

Start Attendance System

View Attendance Records


Uses os.system() to run other Python files


2️⃣ Face Recognition (main.py)

Loads known student images from the folder

Encodes facial features using the face_recognition library

Captures live video through webcam

Matches detected faces with stored encodings

Uses blink detection (eye aspect ratio) to ensure liveness

Marks attendance only once per day for each student

Stores name, date, and time in SQLite database


3️⃣ Attendance Viewer (view_attendance.py)

Built using Tkinter GUI

Fetches records from SQLite database

Allows searching attendance by name

Displays attendance in a table format


🗄️ Database Design

Database Name: attendance.db

Table: attendance

Column	Description

id	Auto-increment primary key
name	Student name
time	Time of attendance
date	Date of attendance


🤖 AI / ML Concepts Used

Face Encoding & Matching

Deep Learning (via dlib internally)

Computer Vision

Liveness Detection using Eye Blink

Pattern Recognition


> Note: This project uses pre-trained models, so no manual training is required.


✅ Features

Real-time face detection and recognition

Blink-based liveness detection

Prevents multiple attendance entries on the same day

Secure local database storage

Simple and clean GUI for viewing attendance

Easy to understand and beginner-friendly


🚀 How to Run the Project

1. Install required libraries:



pip install opencv-python face_recognition mediapipe numpy

2. Run the main menu:

python app.py

3. Choose:

1 → Start Attendance System

2 → View Attendance Records


📌 Applications

Colleges and universities

Schools

Offices

Training institutes

Labs and workshops


🔮 Future Enhancements

Cloud database integration

Web-based dashboard

Multiple face enrollment

Mobile application support

Mask detection

Report export (PDF/Excel)


👨‍🎓 Developed By

Dipendra Joshi
BCA Student
Graphic Era Hill University


📜 License

This project is developed for educational purposes and mini-project submission.


