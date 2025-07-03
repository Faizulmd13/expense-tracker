from datetime import datetime

def add_expense(expenses):
    date = datetime.now().timestamp()
    amount = int(input("Enter the Amount: "))
    category = input("Enter the Category: ")
    description = input("Enter a brief description: ")
    new_expense = {
        "date":date, "amount":amount, "category":category, "description":description
    }
    expenses.append(new_expense)

def view_expenses(expenses):
    for expense in expenses:
        dt = datetime.fromtimestamp(expense["date"])
        print("Data and time: ", dt.strftime("%Y-%m-%d %I:%M %p"))
        print("Amount: ", expense["amount"])
        print("Category: ", expense["category"])
        print("Description: ", expense["description"])
        print()

def summarize_expenses(expenses):
    category_totals = {}
    total = 0
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        total += amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("Total amount spent: ", total)
    print("Spending by category:")
    for category, amount in category_totals.items():
        print(f"    {category}: {amount}")