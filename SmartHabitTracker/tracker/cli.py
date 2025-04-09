import argparse
from tracker import data_handler, visualizer, motivator

def main():
    parser = argparse.ArgumentParser(description="Smart Habit Tracker")
    subparsers = parser.add_subparsers(dest='command')

    add = subparsers.add_parser("add")
    add.add_argument("name", help="Name of the habit")

    log = subparsers.add_parser("log")
    log.add_argument("name", help="Habit to log today")

    streaks = subparsers.add_parser("streaks")

    viz = subparsers.add_parser("visualize")

    args = parser.parse_args()

    if args.command == "add":
        data_handler.add_habit(args.name)
    elif args.command == "log":
        data_handler.log_habit(args.name)
    elif args.command == "streaks":
        data_handler.show_streaks()
    elif args.command == "visualize":
        visualizer.plot_habits()
    else:
        parser.print_help()