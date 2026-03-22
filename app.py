import os
import constant as con
from parser import parser

def main():
    # Create root folder for tracker
    os.makedirs(con.ROOT_TRACKER_DIR, exist_ok=True)

    parser()

if __name__ == "__main__":
    main()
