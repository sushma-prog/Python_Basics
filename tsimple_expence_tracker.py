#defaultdict is a special dictionary from Python’s collections module that automatically initializes values for missing keys.

from collections import defaultdict #It will create a dictionary where each new key will have a default value of float(), which is 0.0.

expenses = []

#function to add an expense
def add_expense():
    category = input("Enter your expense category(for eg. food, shopping, electricity): ")
    amount = float(input(f"enter the expense amount for {category}: ₹"))
    date = (input(f"enter the date when ₹{amount} was used for {category} (for eg. DD-MM-YYYY): "))
    expense = {"category": category, "amount": amount, "date": date}
    expenses.append(expense)
    print(f"Expense of ₹{amount} added successfully for the category '{category}' on the date {date}.\n ")

#function for calculating total expenses
def total_expenses():
    total = sum(expense["amount"]for expense in expenses)
    print(f"Total expenses: ₹{total}\n")

#function to dispaly all expenses
def display_expenses():
    if not expenses:
        print("no expense recorded yet!\n")
        return
    print("\nEXPENSES RECORD:")
    print("\nCategory\tAmount\t\tDate")
    for expense in expenses:
        print(f"\n{expense['category']}\t₹{expense['amount']}\t\t{expense['date']}")
    print()

#function to print most expensive category
def most_expensive_category():
    if not expenses:
        print("No expenses recorder yet!\n")
        return
    category_total = defaultdict(float)
    for expense in expenses:
        category_total[expense['category']] = category_total[expense['category']] + expense['amount']
    most_expensive = max(category_total, key=category_total.get)
    print(f"\nmost expensive category : '{most_expensive}' for total amount ₹{category_total[most_expensive]} ")

#to print menu
while True:
    print("\n--MENU--")
    print("1. add an expense")
    print("2. calculate total expense.")
    print("3. view all expenses.")
    print("4. display most expensive category.")
    print("5. exit.")

    choice = int(input("enter your choice: "))
    if choice == 1:
        add_expense()
    elif choice == 2:
        total_expenses()
    elif choice == 3:
        display_expenses()
    elif choice == 4:
        most_expensive_category()
    elif choice == 5:
        print("exiting the program. thank you!")
        break
    else:
        print("invalid choice. please try again.")