from database import get_user
from auth import authenticate


def load_user(database):
    if authenticate():
        return get_user(database, 1)
    return None


def format_user(user):
    return f"{user['id']} - {user['name']} ({user['email']})"