import argparse

def parser():
    # Create parser for command
    parser = argparse.ArgumentParser(prog="koin", description="Expense Tracker CLI in Python")
    # Create command
    command = parser.add_subparsers(dest="command")

    args = parser.parse_args()

    parser.print_help()

def main():
    parser()

if __name__ == "__main__":
    main()
