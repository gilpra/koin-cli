import argparse
from koin.database import get_transaction_by_id, update_data

def edit_func(args: argparse.Namespace):
    id = int(args.id)
    data_tracker = get_transaction_by_id(id) # Get data transaction based on id

    if not data_tracker:
        print("\nError: ID transaction not found")
        return

    amount = data_tracker["amount"]
    description = data_tracker["description"]
    date = data_tracker["date"]

    # Check input user
    if args.amount:
        amount = args.amount
    if args.description:
        description = args.description
    if args.date:
        date = args.date

    confirm = input("Update this transaction? [Y/n]: ").strip().lower()
    # Confirm logic
    if confirm in ["", "y", "yes"]:
        print(f"\nUpdating data...")
        # Update data tracker
        update_data(id, amount=amount, description=description, date=date)
    else:
        print(f"\nCancel update transaction!")
