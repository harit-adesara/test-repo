from database import getUser
from auth import authenticate


def load_user(database):
    if authenticate():
        return getUser(database, 1)
    return None


def format_user(user):
    return f"{user['id']} - {user['name']} ({user['email']})"