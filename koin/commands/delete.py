import argparse
from koin.database import delete_data

def delete_func(args: argparse.Namespace):
    id = int(args.id)

    confirm = input("Delete this transaction? [Y/n]: ").strip().lower()
    # Confirm logic
    if confirm in ["", "y", "yes"]:
        # Delete data tracker
        try:
            delete_data(id)
            print(f"\nDeleting data...")
        except ValueError as e:
            print(f"\nError: {e}")
    else:
        print(f"\nCancel delete transaction!")
