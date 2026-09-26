# Project Report

**Title:** Hostel Mess Menu Management System

**Name:** [Keshav Srivastava]
**Registration Number:** [26BAI10630]
**Course:** [INTRODUCTION TO PROBLEM SOLVING/ PYTHON ESSENTIALS]
**Semester:** 1
**Institution:** VIT Bhopal University
**Submission Platform:** VITyarthi

---

## 1. Abstract

Hostel students often face confusion about what food is being served on a
particular day, and hostel mess staff have no easy way to track how many
students actually ate a particular meal or what students thought of the food
quality. This project, **Hostel Mess Menu Management System**, is a
command-line Python application that solves this in a simple way. It lets a
user view the weekly mess menu, mark and view student attendance for meals,
and collect feedback/ratings for each meal. The project is built using only
core Python concepts — data types (dictionaries, lists, tuples, strings),
functions, conditionals, loops, and file handling — and is divided into
separate modules to keep the code organized.

## 2. Objective

- To build a working, terminal-based system that manages a hostel mess menu.
- To practice and demonstrate core Python concepts: variables, data types
  (dict, list, tuple, string), functions, loops, conditionals, and file I/O.
- To split the program logic into multiple reusable modules instead of writing
  everything in a single file.
- To make a project that can run on any machine with just Python installed,
  with no external database or GUI dependency.

## 3. Tools and Technologies Used

| Tool / Technology | Purpose |
|---|---|
| Python 3 | Programming language used for the entire project |
| Built-in `os` module | To check whether data files exist before reading |
| Plain text files (`.txt`) | Used to store attendance  data persistently |
| Git & GitHub | Version control and submission of source code |
| VS Code / any text editor | Used to write and edit the code |

No external/third-party libraries were used — the project runs with a
plain Python installation.

## 4. System Modules

The project is divided into 4 files, of which 3 are independent modules
imported into the main program:

### 4.1 `menu_module.py`
Stores the weekly mess menu as a nested dictionary (day → meal → list of food
items). Provides functions to:
- `show_full_menu()` – prints the entire week's menu
- `show_today_menu(day)` – prints menu for one day
- `update_menu(day, meal, new_items)` – lets admin/warden change the menu
- `search_item(item_name)` – finds which day(s)/meal(s) a food item appears in

### 4.2 `attendance_module.py`
Handles marking and tracking student mess attendance, using a text file
(`attendance.txt`) for storage so records persist between runs. Provides:
- `mark_attendance(name, day, meal)` – records a student's attendance
- `view_attendance()` – displays all recorded attendance entries
- `count_attendance(name)` – counts how many times a student has attended



### 4.3 `main.py`
The entry point of the program. Displays a numbered menu in the terminal,
takes the user's choice using `input()`, and calls the appropriate function
from the three modules above inside a `while True` loop until the user
chooses to exit.

## 5. Data Types and Concepts Used

- **Dictionary:** the entire mess menu is stored as a nested dictionary
- **List:** food items per meal, attendance/feedback rows read from file
- **Tuple:** `valid_days` and `valid_meals` are stored as tuples since they
  don't change during the program
- **String methods:** `.strip()`, `.capitalize()`, `.lower()`, `.split()`,
  `.join()` are used throughout for cleaning and formatting user input
- **Functions:** every operation (view, update, search, mark, count, feedback)
  is written as a separate function with parameters and return values
- **File handling:** `open()`, `.write()`, `.readlines()` used to persist
  attendance and feedback data across program runs
- **Conditionals & loops:** `if / elif / else` for menu choices and input
  validation, `while True` for the main program loop, `for` loops to process
  lists/dictionaries
- **Exception handling:** `try / except` used when converting rating input to
  an integer, to avoid the program crashing on bad input

## 6. How the Program Works (Flow)

1. Program starts by running `main.py`.
2. The main menu with 10 options + exit is displayed in a loop.
3. Based on the number entered, the corresponding function from
   `menu_module`, `attendance_module`,  is called.
4. User input is collected using `input()` and passed as arguments to these
   functions.
5. Menu data lives in memory (dictionary) for the duration of the run.
   Attendance and feedback data are written to and read from text files so
   they are not lost when the program closes.
6. The loop continues until the user enters `0`, which exits the program.

## 7. Sample Output

```
===================================
 HOSTEL MESS MENU MANAGEMENT SYSTEM
===================================
1. View full week menu
2. View today's / a specific day's menu
3. Update menu (admin/warden use)
4. Search for a food item
5. Mark mess attendance
6. View attendance records
7. Check a student's attendance count
8. Exit
Enter your choice: 2
Enter the day (e.g. Monday): Monday

----- MENU FOR MONDAY -----
Breakfast : Poha, Tea, Banana
Lunch : Rice, Dal, Mix Veg, Roti
Dinner : Roti, Paneer Curry, Salad
```

*(Add your own terminal screenshots here before submission.)*

## 8. Limitations

- Data is stored in plain text files, not a proper database, so it is not
  suitable for large-scale/multi-user simultaneous access.
- No login/authentication system — anyone running the program can update the
  menu.
- No GUI — the project is intentionally command-line only, as required by
  the submission guidelines.

## 9. Future Scope

- Add a login system separating student/warden access.
- Move data storage from text files to SQLite for better reliability.
- Add a simple web or GUI interface using Flask/Tkinter.
- Auto-detect the current day using Python's `datetime` module instead of
  asking the user to type it.

## 10. Conclusion

This project helped apply core Python concepts — data types, functions, loops,
conditionals, and file handling — to build a small but complete real-world
utility for hostel mess management. Splitting the code into separate modules
made it easier to test, understand, and maintain each part of the system
independently. The project fully runs from the command line with no external
dependencies, meeting all the submission requirements.

## 11. GitHub Repository Link
https://github.com/KESHAVSRIVASTAVA1/Hostel-mess-management-system
