import argparse
from database import delete_data

def delete_func(args: argparse.Namespace):
    id = int(args.id)

    confirm = input("Delete this transaction? [Y/n]: ").strip().lower()
    # Confirm logic
    if confirm in ["", "y", "yes"]:
        print(f"\nDeleting data...")
        # Delete data tracker
        delete_data(id)
    else:
        print(f"\nCancel delete transaction!")
