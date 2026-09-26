# menu_module.py
# This file handles everything related to the weekly mess menu.
# The menu is stored as a dictionary (dict data type) where:
#   key   -> day of the week (string)
#   value -> another dictionary with breakfast, lunch and dinner (lists of strings)

# main menu data, this is what gets shown / edited by the program
mess_menu = {
    "Monday":    {"breakfast": ["Poha", "Tea", "Banana"], "lunch": ["Rice", "Dal", "Mix Veg", "Roti"], "dinner": ["Roti", "Paneer Curry", "Salad"]},
    "Tuesday":   {"breakfast": ["Idli", "Sambhar", "Coffee"], "lunch": ["Rice", "Rajma", "Roti", "Curd"], "dinner": ["Fried Rice", "Manchurian"]},
    "Wednesday": {"breakfast": ["Bread Omlette", "Tea"], "lunch": ["Rice", "Chole", "Roti", "Salad"], "dinner": ["Roti", "Aloo Gobi", "Dal"]},
    "Thursday":  {"breakfast": ["Paratha", "Curd", "Tea"], "lunch": ["Rice", "Sambhar", "Roti"], "dinner": ["Pulao", "Raita"]},
    "Friday":    {"breakfast": ["Upma", "Coffee"], "lunch": ["Rice", "Kadhi Pakora", "Roti"], "dinner": ["Roti", "Chana Masala", "Rice"]},
    "Saturday":  {"breakfast": ["Chole Bhature"], "lunch": ["Veg Biryani", "Raita"], "dinner": ["Roti", "Mix Veg", "Soup"]},
    "Sunday":    {"breakfast": ["Chole Bhature", "Lassi"], "lunch": ["Special Thali"], "dinner": ["Pizza", "Cold Drink"]}
}

# just a tuple of valid days, used to check user input
valid_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# just a tuple of valid meal times
valid_meals = ("breakfast", "lunch", "dinner")


def show_full_menu():
    # prints the whole week menu
    print("\n----- FULL WEEK MESS MENU -----")
    for day in mess_menu:
        print("\n" + day)
        for meal in mess_menu[day]:
            items = ", ".join(mess_menu[day][meal])   # list -> string
            print("  " + meal.capitalize() + " : " + items)


def show_today_menu(day):
    # day is a string like "Monday"
    day = day.strip().capitalize()
    if day not in valid_days:
        print("Invalid day entered. Please enter a proper day name like Monday.")
        return

    print("\n----- MENU FOR " + day.upper() + " -----")
    for meal in mess_menu[day]:
        items = ", ".join(mess_menu[day][meal])
        print(meal.capitalize() + " : " + items)


def update_menu(day, meal, new_items):
    # new_items should be a list of strings
    day = day.strip().capitalize()
    meal = meal.strip().lower()

    if day not in valid_days:
        print("Invalid day.")
        return False
    if meal not in valid_meals:
        print("Invalid meal type. Choose from breakfast, lunch, dinner.")
        return False

    mess_menu[day][meal] = new_items
    print("Menu updated for " + day + " " + meal + ".")
    return True


def search_item(item_name):
    # searches the whole week to see which day/meal has a particular food item
    item_name = item_name.strip().lower()
    found_in = []   # empty list to collect results

    for day in mess_menu:
        for meal in mess_menu[day]:
            for food in mess_menu[day][meal]:
                if item_name == food.lower():
                    found_in.append((day, meal))   # tuple added to list

    if len(found_in) == 0:
        print("'" + item_name + "' was not found in this week's menu.")
    else:
        print("'" + item_name + "' is served on:")
        for entry in found_in:
            print("  " + entry[0] + " - " + entry[1])

    return found_in
