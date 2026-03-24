import argparse
from database import read_database

def list_func(args: argparse.Namespace):
    data_tracker = read_database()
    print(f"{'ID':<6}{'DATE':<12}{'TYPE':<11}{'CATEGORY':<11}{'AMOUNT':>12}")
    print("-" * 52)

    for transaction in data_tracker:
        print(
            f"{transaction['id']:<6}"
            f"{transaction['date']:<12}"
            f"{transaction['type'].upper():<11}"
            f"{transaction['category'].title():<11}"
            f"{transaction['amount']:>12}"
        )

    print("-" * 52)
    print(f"Total transactions: {len(data_tracker)}")


