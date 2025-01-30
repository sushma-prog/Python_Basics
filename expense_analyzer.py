from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def read_expenses(filename):
    expenses = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    log_message(f"skipping invalid line: {line.strip()}")
                    continue
                try:
                    category = parts[0].split(":")[1]
                    amount = float(parts[1].split(":")[1])
                    date = parts[2].split(":")[1] 
                    expenses.append((category, amount, date))
                except (IndexError, ValueError):
                    log_message(f"skipping malformed line: {line.strip()}")

    except FileNotFoundError:
        log_message(f"file {filename} not found. add some expenses first.")

    return expenses
 
def analyze_expenses(expenses):
    category_totals = {}
    for category, amount, _ in expenses:
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return category_totals

def display_summary(category_totals):
    print("\n--- Expense Summary ---")

    for category, total in category_totals.items():
        print(f"{category}: Rs.{total:.2f}")

    if category_totals:
        most_expensive = max(category_totals, key=category_totals.get)
        print(f"\nMost expensive: '{most_expensive}' with total Rs{category_totals[most_expensive]}")

filename = input("Enter the expense file name (default: expense.txt): ").strip() or "expense.txt"
expenses = read_expenses("expense.txt")
if expenses:
    category_totals = analyze_expenses(expenses)
    display_summary(category_totals)
else:
    log_message("No expenses to analyze")