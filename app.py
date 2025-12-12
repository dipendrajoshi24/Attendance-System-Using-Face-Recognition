import os

print("1. Start Attendance System")
print("2. View Attendance Records")
choice = input("Enter choice: ")

if choice == "1":
    os.system("python main.py")
elif choice == "2":
    os.system("python view_attendance.py")
