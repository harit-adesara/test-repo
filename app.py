from database import connect_database
from utils import load_user
from logger import log

def main():
    log("Application Started")

    conn = connect_database()
    print("Database Connected")

    user = load_user(conn)
    print(user)

    log("Application Finished")


if __name__ == "__main__":
    main()