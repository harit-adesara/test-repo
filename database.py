DATABASE = {
    1: {
        "id": 1,
        "name": "Harit",
        "email": "harit@example.com"
    },
    2: {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com"
    }
}


def connect_database():
    return DATABASE


def get_user(database, user_id):
    return database.get(user_id)