import json
from datetime import datetime
from pathlib import Path
import storage
import tracker
import sys

file_path = Path("expense.json")

expenses = storage.load_data(file_path)

while(1):
    print("1. Add a spending")
    print("2. View all the Spendings")
    print("3. Summarize")
    print("4. Exit")
    choice = int(input("Enter your Choice: "))

    if choice == 1:
        tracker.add_expense(expenses)
        storage.save_data(expenses, file_path)
    elif choice == 2:
        tracker.view_expenses(expenses)
    elif choice == 3:
        tracker.summarize_expenses(expenses)
    elif choice == 4:
        print("Exiting the expense tracker")
        sys.exit()
    else:
        print("Invalid Choice")
    


