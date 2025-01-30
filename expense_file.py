"""we need to import datetime module from python's built-in datetime library."""
from datetime import datetime
"""we need datetime to get the current date and time."""

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def save_to_file(filename,data):
    with open(filename, "a") as file:
        file.write(data + "\n")
    log_message(f"data save to {filename}")

def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            contents = file.readlines()
            for line in contents:
                print(line.strip())
    except FileNotFoundError:
        log_message(f"file {filename} not found.")

def add_expense():
    category = input("enter the category of expense (eg. food, shopping, travelling): ")
    amount = float(input("enter the amount: Rs."))
    date = input("enter date (YYYY-MM-DD): ")
    data = f"category:{category}, amount:{amount}, date:{date}"
    save_to_file("expense.txt", data)

while True:
    print("\n--MENU--")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        read_from_file("expense.txt")
    elif choice == "3":
        print("thank you for using the system. see you!")
        break
    else:
        print("invalid choice, try again!")