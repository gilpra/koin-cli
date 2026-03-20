import argparse

def parser():
    # Create parser for command
    parser = argparse.ArgumentParser(prog="koin", description="Expense Tracker CLI in Python")
    # Create command
    command = parser.add_subparsers(dest="command")

    # Add command
    command.add_parser("add", help="Add a transaction")

    args = parser.parse_args()

    # Check command input
    command_input = args.command
    if command_input == "add":
        print("Run add function")
    else:
        parser.print_help()

def main():
    parser()

if __name__ == "__main__":
    main()
