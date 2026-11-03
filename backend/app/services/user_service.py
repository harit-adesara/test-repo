from app.errors import NotFoundError
from app.repositories import user_repository
from app.services.auth_service import public_user


def get_user(user_id):
    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise NotFoundError("User not found")
    return public_user(user)


def list_users():
    return [public_user(user) for user in user_repository.list_users()]
