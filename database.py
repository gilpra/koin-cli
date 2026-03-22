import os
import json
from datetime import datetime
import constant as con

# Read database
def read_database() -> list:
    # Check if database exist
    if not os.path.exists(con.DATABASE_PATH):
        return []

    # Read database
    with open(con.DATABASE_PATH, "r") as file:
        return json.load(file)

def store_data(type: str, amount: float, category: str, description: str, date: str):
    date_now = datetime.now()# Get time now
    data_tracker = read_database() # Read data from database
    last_id = 0

    if data_tracker:
        last_id = data_tracker[-1].get("id", 0)

    # Set dict for new transaction
    new_transaction = {
              "id": last_id + 1,
              "type": type,
              "amount": amount,
              "category": category,
              "description": description,
              "date": date,
              "created_at": date_now.isoformat()
           }

    # Append data new transaction to data_tracker
    data_tracker.append(new_transaction)

    # Seriazed data_tracker before write to json
    serialized_data = json.dumps(data_tracker, indent=2)

    # Write data_tracker to json
    with open(con.DATABASE_PATH, 'w', encoding="utf-8") as file:
        file.write(serialized_data)


