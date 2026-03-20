import argparse
from datetime import datetime
import os
import json

ROOT_TRACKER_DIR = os.path.expanduser("~/.local/share/koin")
DATABASE_PATH = os.path.join(ROOT_TRACKER_DIR, "tracker.json")

# Read database
def read_database() -> dict:
    # Check if database exist
    if not os.path.exists(DATABASE_PATH):
        return {}

    # Read database
    with open(DATABASE_PATH, "r") as file:
        return json.load(file)

def store_data(type: str, amount: float, category: str, description: str, date: str):
    date_now = datetime.now()# Get time now
    data_tracker = [] # Read data from database

    # Set dict for new transaction
    new_transaction = {
              "id": 1,
              "type": type,
              "amount": amount,
              "category": category,
              "description": description,
              "date": date,
              "created_at": date_now.isoformat()
           }

    # Append data new transaction to data_tracker
    data_tracker.append(new_transaction)

    # Seriazed data_tracker before write to json
    serialized_data = json.dumps(data_tracker, indent=2)

    # Write data_tracker to json

# Function create subcommand for command "add"
def create_subcommand_add(parser: argparse._SubParsersAction, name: str, help: str):
    VALID_CATEGORY={
        "expense": ["food", "transport", "shopping", "biils", "other"],
        "income": ["salary", "business", "investment", "gift", "other"]
    }

    subcommand = parser.add_parser(name, help=help)

    # Create argument
    subcommand.add_argument("--amount", "-a", required=True, type=float)
    subcommand.add_argument("--category", "-c", default="other", choices=VALID_CATEGORY[name])
    subcommand.add_argument("--description", "-d", default="")
    subcommand.add_argument("--date", required=True)

    subcommand.set_defaults(func=add_func)

def add_func(args: argparse.Namespace):
    # Variable
    type_input = args.subcommand
    amount_input = args.amount
    category_input = args.category
    description_input = args.description
    date_input = args.date

    # Print confirmation store data
    print("\n" + "=" * 36)
    print("      TRANSACTION CONFIRMATION")
    print("=" * 36)

    print(f"{'Type':<12}: {type_input.title()}")
    print(f"{'Amount':<12}: {amount_input}")
    print(f"{'Category':<12}: {category_input.title()}")
    print(f"{'Description':<12}: {description_input or '-'}")
    print(f"{'Date':<12}: {date_input}")

    print("=" * 36)

    confirm = input("Save this transaction? [Y/n]: ").strip().lower()

    # Confirm logic
    if confirm in ["", "y", "yes"]:
        print("\nStoring data...")
        store_data(type=type_input,
           amount=amount_input,
           category=category_input,
           description=description_input,
           date=date_input)
    else:
        print(f"\nCancel transaction!")


def parser():
    # Create parser for command
    parser = argparse.ArgumentParser(prog="koin", description="Expense Tracker CLI in Python")
    # Create command
    command = parser.add_subparsers(dest="command")

    # Add command
    add_command = command.add_parser("add", help="Add a transaction")
    add_subcommand = add_command.add_subparsers(dest="subcommand")
    create_subcommand_add(add_subcommand, "expense", "Add Expense to tracker")
    create_subcommand_add(add_subcommand, "income", "Add Income to tracker")

    args = parser.parse_args()

    # Check command input
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

def main():
    # Create root folder for tracker
    os.makedirs(ROOT_TRACKER_DIR, exist_ok=True)

    parser()

if __name__ == "__main__":
    main()
