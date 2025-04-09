import matplotlib.pyplot as plt
import json
from datetime import datetime

def plot_habits():
    with open("habits.json", "r") as f:
        data = json.load(f)

    for habit, info in data.items():
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in info["logs"]]
        dates.sort()
        counts = list(range(1, len(dates)+1))
        plt.plot(dates, counts, label=habit)

    plt.title("Habit Progress Over Time")
    plt.xlabel("Date")
    plt.ylabel("Times Completed")
    plt.legend()
    plt.tight_layout()
    plt.savefig("habit_progress.png")
    plt.show()