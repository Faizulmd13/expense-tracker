# 🧾 Expense Tracker (CLI-based)

A simple command-line expense tracker written in Python. It helps you record daily expenses, view them, and summarize spending across categories. Data is saved to a local JSON file.

## ✨ Features

- Add a new expense with amount, category, and description.
- View all recorded expenses.
- Get a summary of total and category-wise spendings.
- Data is stored in a local `expense.json` file.

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed

### Run the application

git clone <your-repo-url>
cd <your-project-folder>
python main.py

### 🗂️ Project Structure

.
├── main.py           # Main menu loop for the CLI
├── storage.py        # Handles saving and loading expense data
├── tracker.py        # Contains functions to add, view, and summarize expenses
└── expense.json      # Stores expense data as JSON

### 🛠️ Usage

When you run main.py, you'll see a menu like:

1. Add a spending
2. View all the Spendings
3. Summarize
4. Exit
Choose an option by entering a number. For example:

Press 1 to add a new spending.

Press 2 to see all expenses.

Press 3 for a summary.

Press 4 to exit.

### 📝 Sample Data

expense.json includes some pre-filled example expenses:

[
  {
    "date": 1751520481.396358,
    "amount": 500,
    "category": "Cash",
    "description": "Lunch with friends"
  },
  {
    "date": 1751522705.360264,
    "amount": 330,
    "category": "Gpay",
    "description": "Petrol price"
  },
  {
    "date": 1751523748.833402,
    "amount": 199,
    "category": "Gpay",
    "description": "Mom's recharge"
  }
]
