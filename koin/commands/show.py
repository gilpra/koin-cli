import argparse
from koin.database import get_transaction_by_id

def show_func(args: argparse.Namespace):
    detail_transaction = get_transaction_by_id(int(args.id))

    print("\nTransaction Details")
    print("-" * 40)
    print(f"{'ID':<12}: {detail_transaction['id']}")
    print(f"{'Type':<12}: {detail_transaction["type"].title()}")
    print(f"{'Amount':<12}: {detail_transaction["amount"]}")
    print(f"{'Category':<12}: {detail_transaction["category"].title()}")
    print(f"{'Description':<12}: {detail_transaction["description"] or '-'}")
    print(f"{'Date':<12}: {detail_transaction["date"]}")
    print("-" * 40)
