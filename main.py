import cv2
import face_recognition
import numpy as np
import os
import sqlite3
from datetime import datetime
import mediapipe as mp
from math import hypot

# ---------------- DATABASE SETUP ---------------- #
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    time TEXT,
    date TEXT
)
""")
conn.commit()

# ---------------- LIVENESS (BLINK) SETUP ---------------- #
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

LEFT = [33,160,158,133,153,144]
RIGHT = [362,385,387,263,373,380]

def get_EAR(lm, eye):
    p = [lm[i] for i in eye]
    v1 = hypot(p[1].x - p[5].x, p[1].y - p[5].y)
    v2 = hypot(p[2].x - p[4].x, p[2].y - p[4].y)
    h = hypot(p[0].x - p[3].x, p[0].y - p[3].y)
    return (v1 + v2) / (2.0 * h)

blink_count = 0
blink_ok = False

# ---------------- LOAD STUDENT FACES ---------------- #
known_encodings, known_names = [], []

for img_name in os.listdir("students"):
    if img_name.lower().endswith((".jpg",".png",".jpeg")):
        img = face_recognition.load_image_file("students/" + img_name)
        enc = face_recognition.face_encodings(img)
        if enc:
            known_encodings.append(enc[0])
            known_names.append(os.path.splitext(img_name)[0])

# ---------------- ATTENDANCE LOG FUNCTION ------------- #
def mark_attendance(name):
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    cursor.execute("SELECT * FROM attendance WHERE name=? AND date=?", (name, date))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO attendance (name,time,date) VALUES (?,?,?)",
                        (name,time,date))
        conn.commit()
        print(f"[MARKED] {name} at {time}")

# ---------------- CAMERA LOOP ---------------- #
cap = cv2.VideoCapture(0)
print("[INFO] Blink to verify identity...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    r = face_mesh.process(rgb)

    if r.multi_face_landmarks:
        lm = r.multi_face_landmarks[0].landmark
        ear = (get_EAR(lm, LEFT) + get_EAR(lm, RIGHT)) / 2

        if ear < 0.25: blink_count += 1
        else:
            if blink_count > 2: blink_ok = True
            blink_count = 0

    if blink_ok:
        small = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
        rgb_small = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(rgb_small)
        encs = face_recognition.face_encodings(rgb_small, faces)

        for (top,right,bottom,left), enc in zip(faces, encs):
            name = "Unknown"
            matches = face_recognition.compare_faces(known_encodings, enc)
            if True in matches:
                d = face_recognition.face_distance(known_encodings, enc)
                i = np.argmin(d)
                if d[i] < 0.48:
                    name = known_names[i]
                    mark_attendance(name)

            top,right,bottom,left = top*4,right*4,bottom*4,left*4
            cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
            cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

        blink_ok = False

    cv2.imshow("Attendance System (Blink First)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
