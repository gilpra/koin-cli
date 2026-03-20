import argparse

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
        print("Store data")
    else:
        print("Cancel")

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
    parser()

if __name__ == "__main__":
    main()
