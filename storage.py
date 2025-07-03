import json

def load_data(file_path):
    if not file_path.exists() or file_path.read_text().strip() == "":
        file_path.write_text("[]")

    try:
        expenses = json.loads(file_path.read_text())
    except json.JSONDecodeError:
        expenses = []
        file_path.write_text("[]")

    return expenses

def save_data(expenses, file_path):
    exp = json.dumps(expenses, indent=4)
    file_path.write_text(exp)