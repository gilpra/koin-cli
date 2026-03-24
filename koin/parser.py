import argparse
import datetime
from koin.commands.add import add_func
from koin.commands.list import list_func
from koin.commands.show import show_func
from koin.commands.edit import edit_func
from koin.commands.delete import delete_func
from koin.constant import VALID_CATEGORY

# Function create subcommand for command "add"
def create_subcommand_add(parser: argparse._SubParsersAction, name: str, help: str):
    subcommand = parser.add_parser(name, help=help)

    # Create argument
    subcommand.add_argument("--amount", "-a", required=True, type=float)
    subcommand.add_argument("--category", "-c", default="other", choices=VALID_CATEGORY[name])
    subcommand.add_argument("--description", "-d", default="")
    subcommand.add_argument("--date", required=True, type=datetime.date.fromisoformat)

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

    # List command
    list_command = command.add_parser("list", help="List transactions")
    list_command.set_defaults(func=list_func)

    # Show command
    show_command = command.add_parser("show", help="Show transaction details")
    show_command.add_argument("id", help="ID transaction")
    show_command.set_defaults(func=show_func)

    # Edit command
    edit_command = command.add_parser("edit", help="Edit a transaction")
    edit_command.add_argument("id", help="ID transaction", type=int)
    edit_command.add_argument("--amount", "-a", type=float)
    edit_command.add_argument("--description", "-d", default="")
    edit_command.add_argument("--date")
    edit_command.set_defaults(func=edit_func)

    # Delete command
    delete_command = command.add_parser("delete", help="Delete a transaction")
    delete_command.add_argument("id", help="ID transaction", type=int)
    delete_command.set_defaults(func=delete_func)

    args = parser.parse_args()

    # Check command input
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

