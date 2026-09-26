# Hostel Mess Menu Management System

A simple command-line Python project to manage a hostel mess menu — students can view
the weekly menu, mark their mess attendance, and give feedback/ratings for meals.
Made as a first-semester mini project using core Python (data types, functions, and
multiple modules).

## Features

- View the full week's mess menu
- View menu for a specific day
- Update the menu (for warden/admin use)
- Search which day/meal a food item is served in
- Mark student attendance for a meal (saved to a text file)
- View all attendance records
- Check how many times a particular student has attended the mess

## Project Structure

```
hostel-mess-menu-management/
│
├── main.py                 # entry point, run this file to start the program
├── menu_module.py           # handles the weekly menu (view/update/search)
├── attendance_module.py     # handles marking and viewing mess attendance
├── .gitignore
└── README.md
```

Two data files, `attendance.txt` and `feedback.txt`, are created automatically the
first time you mark attendance or give feedback. They are not included in the repo
since they get generated at runtime (see `.gitignore`).

## Requirements

- Python 3.7 or above (no external libraries needed — only Python's built-in
  modules are used)

## Setup Instructions

1. **Install Python** (if not already installed)
   - Download from [python.org/downloads](https://www.python.org/downloads/)
   - During installation on Windows, make sure to check "Add Python to PATH"
   - Verify installation by running:
     ```
     python --version
     ```
     or on some systems:
     ```
     python3 --version
     ```

2. **Clone this repository**
   ```
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
   (Or simply download the ZIP from GitHub and extract it, then open a terminal
   inside the extracted folder.)

3. **No extra dependencies to install** — this project only uses Python's
   standard library (`os`), so there is no `requirements.txt` needed.

## How to Run

From inside the project folder, run:

```
python main.py
```

or, depending on your system:

```
python3 main.py
```

You will see a numbered menu in the terminal like this:

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
Enter your choice:
```

Type the number of the option you want and press Enter. Follow the prompts
(e.g., enter a day like `Monday`, a meal like `lunch`, etc.). Choose `0` to exit
the program.

## Example Usage

- To see Monday's menu: choose option `2`, then type `Monday`
- To mark your attendance: choose option `5`, then enter your name, the day,
  and the meal (breakfast/lunch/dinner)

## Notes

- Attendance and feedback data are stored in plain text files (`attendance.txt`) in the same folder, in comma-separated format. These are
  created automatically the first time you use those options — no manual setup
  needed.
- This project does not use any database or external package on purpose, to
  keep it simple and runnable on any machine with plain Python installed.

## Author

Keshav Srivastava
 VIT Bhopal — Semester 1 Mini Project
