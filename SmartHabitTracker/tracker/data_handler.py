import json
from datetime import date

FILE = "habits.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_habit(name):
    data = load_data()
    if name in data:
        print(f"Habit '{name}' already exists.")
    else:
        data[name] = {"logs": []}
        save_data(data)
        print(f"Habit '{name}' added.")

def log_habit(name):
    data = load_data()
    if name not in data:
        print(f"No such habit: {name}")
        return
    today = str(date.today())
    if today in data[name]["logs"]:
        print("Already logged today.")
    else:
        data[name]["logs"].append(today)
        save_data(data)
        print(f"Habit '{name}' logged for today.")

def show_streaks():
    data = load_data()
    for habit, info in data.items():
        logs = sorted(info["logs"])
        print(f"Habit: {habit} | Total logs: {len(logs)}")