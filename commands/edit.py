import argparse
from database import get_transaction_by_id, update_data

def edit_func(args: argparse.Namespace):
    id = int(args.id)
    data_tracker = get_transaction_by_id(id) # Get data transaction based on id

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

    # Update data tracker
    update_data(id, amount=amount, description=description, date=date)
