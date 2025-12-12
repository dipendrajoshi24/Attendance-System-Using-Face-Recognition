import sqlite3
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Attendance Viewer")
root.geometry("600x400")

tree = ttk.Treeview(root, columns=("Name","Time","Date"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Time", text="Time")
tree.heading("Date", text="Date")
tree.pack(fill=tk.BOTH, expand=True)

def load():
    for row in tree.get_children(): tree.delete(row)
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, time, date FROM attendance")
    rows = cursor.fetchall()
    conn.close()
    for r in rows: tree.insert("", tk.END, values=r)

btn = tk.Button(root, text="Refresh", command=load)
btn.pack(pady=10)

load()
root.mainloop()
