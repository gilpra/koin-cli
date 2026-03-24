from koin.parser import parser
from koin.database import initial_database

def main():
    initial_database()
    parser()

if __name__ == "__main__":
    main()
