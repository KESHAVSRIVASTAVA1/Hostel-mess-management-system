# this file's name is  main.py
#  it is  based on Hostel Mess Menu Management System
# This is the main file. we will Run this file to start the program.
# It will use the functions from menu_module, attendance_module and feedback_module.

import menu_module
import attendance_module


def print_main_menu():
    print("\n===================================")
    print(" hostel mess menu management system ")
    print("===================================")
    print("1. see full week menu ")
    print("2. View today's / a specific day's menu")
    print("3. Update menu (admin/warden use)")
    print("4. Search for a food item")
    print("5. Mark mess attendance")
    print("6. View attendance records")
    print("7. Check a student's attendance count")
    print("8. Exit")


def main():
    while True:
        print_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            menu_module.show_full_menu()

        elif choice == "2":
            day = input("Enter the day (e.g. Monday): ")
            menu_module.show_today_menu(day)

        elif choice == "3":
            day = input("Enter day to update: ")
            meal = input("Enter meal (breakfast/lunch/dinner): ")
            items_input = input("Enter new food items separated by comma: ")
            new_items = items_input.split(",")
            # remove extra spaces from each item
            new_items = [item.strip() for item in new_items]
            menu_module.update_menu(day, meal, new_items)

        elif choice == "4":
            item = input("Enter food item to search: ")
            menu_module.search_item(item)

        elif choice == "5":
            name = input("Enter student name: ")
            day = input("Enter day: ")
            meal = input("Enter meal (breakfast/lunch/dinner): ")
            attendance_module.mark_attendance(name, day, meal)

        elif choice == "6":
            attendance_module.view_attendance()

        elif choice == "7":
            name = input("Enter student name: ")
            attendance_module.count_attendance(name)

        elif choice == "8":
            print("Exiting program. Have a good meal!")
            break

        else:
            print("Invalid choice, please try again.")


# this  will make sure the program  will only run when this file is run directly
if __name__ == "__main__":
    main()
