# attendance_module.py
# This file handles marking mess attendance for students.
# Data is stored in a plain text file called attendance.txt so it stays
# saved even after the program is closed (no database used, kept simple).

import os

ATTENDANCE_FILE = "attendance.txt"


def mark_attendance(name, day, meal):
    # name -> string, day -> string, meal -> string
    name = name.strip()
    day = day.strip().capitalize()
    meal = meal.strip().lower()

    if name == "":
        print("Name cannot be empty.")
        return False

    # open in append mode so old records are not lost
    file = open(ATTENDANCE_FILE, "a")
    line = name + "," + day + "," + meal + "\n"
    file.write(line)
    file.close()

    print("Attendance marked for " + name + " (" + day + " " + meal + ")")
    return True


def view_attendance():
    # reads the file and prints every record
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records yet.")
        return []

    file = open(ATTENDANCE_FILE, "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No attendance records yet.")
        return []

    print("\n----- ATTENDANCE RECORDS -----")
    records = []
    count = 1
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")   # parts is a list: [name, day, meal]
        print(str(count) + ". " + parts[0] + " - " + parts[1] + " - " + parts[2])
        records.append(parts)
        count += 1

    return records


def count_attendance(name):
    # counts how many times a particular student has eaten in the mess
    name = name.strip().lower()

    if not os.path.exists(ATTENDANCE_FILE):
        print("No records found.")
        return 0

    file = open(ATTENDANCE_FILE, "r")
    lines = file.readlines()
    file.close()

    total = 0
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) > 0 and parts[0].lower() == name:
            total = total + 1

    print(name.title() + " has attended the mess " + str(total) + " time(s).")
    return total
