#  Attendance System Using Face Recognition
## 📌 Project Overview

The  Attendance   System Using Face Recognition is a smart and automated solution that records attendance using facial recognition technology.It eliminates manual attendance processes, minimizes proxy attendance, and improves accuracy by identifying individuals through their unique facial features in real time.

The system is developed using Python and integrates concepts of Computer Vision, Artificial Intelligence, and Database Management to provide a reliable, secure, and user-friendly attendance solution.

**🎯 Objectives**

Automate the attendance marking process

Prevent proxy and duplicate attendance

Store attendance records securely

Provide an easy interface to view attendance data

Enable a contactless and efficient attendance system

---

**🧠** Technologies & Libraries Used

**🔹** Programming Language

Python – Core language used to develop the system


**🔹 Libraries**

*OpenCV (cv2)* – Captures real-time video and processes images

face_recognition – Detects and recognizes faces using deep learning

MediaPipe – Performs facial landmark detection for blink (liveness) verification

NumPy – Handles numerical and array-based operations

SQLite3 – Stores attendance data in a local database

Tkinter – Provides a simple graphical user interface to view attendance

OS Module – Executes Python files and manages system-level operations

**Datetime** – Records date and time of attendance

---

**🧩 Project Structure**

# Attendance-System-Using-Face-Recognition/
│
├── app.py                 # Main menu (Start system / View attendance)
├── main.py                # Face recognition & attendance marking logic
├── view_attendance.py     # GUI for displaying attendance records
├── attendance.db          # SQLite database (auto-created)
├── dipendra.jpg           # Sample student image
├── README.md              # Project documentation

---

**⚙️ How the System Works**

# 1️⃣ App Menu (app.py)

Displays two options:

Start Attendance System

View Attendance Records


Uses os.system() to execute other Python files

---

# 2️⃣ Face Recognition Module (main.py)

Loads known student images from the dataset

Encodes facial features using the face_recognition library

Captures live video through the webcam

Matches detected faces with stored encodings

Uses blink detection (Eye Aspect Ratio) to verify liveness

Marks attendance only once per day for each student

Stores name, date, and time in the SQLite database

---

# 3️⃣ Attendance Viewer (view_attendance.py)

Built using Tkinter GUI

Fetches attendance records from the database

Allows searching attendance by student name

Displays data in a tabular format


---

**🗄️ Database Design**

Database Name: attendance.db
Table Name: attendance

Column	Description

id	Auto-increment primary key
name	Student name
time	Time of attendance
date	Date of attendance



---

🤖 AI / ML Concepts Used

Face Encoding and Matching

Deep Learning (internally via dlib)

Computer Vision

Liveness Detection using Eye Blink

Pattern Recognition


> Note: This project uses pre-trained models, so no manual model training is required.




---

✅ Features

Real-time face detection and recognition

Blink-based liveness verification

Prevents multiple attendance entries on the same day

Secure local database storage

Simple and clean GUI

Beginner-friendly and easy to understand



---

🚀 How to Run the Project

1️⃣ Install Required Libraries

pip install opencv-python face_recognition mediapipe numpy

2️⃣ Run the Application

python app.py

3️⃣ Choose an Option

1 → Start Attendance System

2 → View Attendance Records


---

📌 Applications

Colleges and Universities

Schools

Offices

Training Institutes

Laboratories and Workshops

---

🔮 Future Enhancements

Cloud database integration

Web-based attendance dashboard

Multiple face enrollment support

Mobile application version

Mask detection support

Attendance report export (PDF / Excel)

---

👨‍🎓 Developed By

Dipendra Joshi
BCA Student
Graphic Era Hill University

📜 License

This project is developed for educational purposes and mini-project submission only.


