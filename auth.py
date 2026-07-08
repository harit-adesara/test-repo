from config import API_KEY


def authenticate():
    if API_KEY:
        return True
    return False