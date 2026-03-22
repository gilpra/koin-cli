import argparse
from database import store_data

def add_func(args: argparse.Namespace):
    # Variable
    type_input = args.subcommand
    amount_input = args.amount
    category_input = args.category
    description_input = args.description
    date_input = args.date

    # Print confirmation store data
    print("\n" + "=" * 36)
    print("      TRANSACTION CONFIRMATION")
    print("=" * 36)

    print(f"{'Type':<12}: {type_input.title()}")
    print(f"{'Amount':<12}: {amount_input}")
    print(f"{'Category':<12}: {category_input.title()}")
    print(f"{'Description':<12}: {description_input or '-'}")
    print(f"{'Date':<12}: {date_input}")

    print("=" * 36)

    confirm = input("Save this transaction? [Y/n]: ").strip().lower()

    # Confirm logic
    if confirm in ["", "y", "yes"]:
        print(f"\nStoring data...")
        store_data(type=type_input,
           amount=amount_input,
           category=category_input,
           description=description_input,
           date=date_input)
    else:
        print(f"\nCancel transaction!")

