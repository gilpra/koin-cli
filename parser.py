import argparse
from commands.add import add_func
from constant import VALID_CATEGORY

# Function create subcommand for command "add"
def create_subcommand_add(parser: argparse._SubParsersAction, name: str, help: str):
    subcommand = parser.add_parser(name, help=help)

    # Create argument
    subcommand.add_argument("--amount", "-a", required=True, type=float)
    subcommand.add_argument("--category", "-c", default="other", choices=VALID_CATEGORY[name])
    subcommand.add_argument("--description", "-d", default="")
    subcommand.add_argument("--date", required=True)

    subcommand.set_defaults(func=add_func)

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

