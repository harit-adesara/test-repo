from app.errors import AuthenticationError, ConflictError
from app.logger import get_logger
from app.repositories import user_repository
from app.utils.security import (
    decode_token,
    generate_token,
    hash_password,
    verify_pasword,
)
from app.utils.validators import validate_email, validate_name, validate_password

logger = get_logger(__name__)


def public_user(user):
    return {"id": user["id"], "name": user["name"], "email": user["email"]}


def register_user(name, email, password):
    name = validate_name(name)
    email = validate_email(email)
    validate_password(password)

    if user_repository.get_user_by_email(email):
        raise ConflictError("Email is already registered")

    user = user_repository.create_user(name, email, hash_password(password))
    logger.info("Registered user id=%s", user["id"])
    return public_user(user)


def login_user(email, password):
    email = validate_email(email)
    user = user_repository.get_user_by_email(email)

    if not user or not verify_pasword(password, user["password_hash"]):
        raise AuthenticationError("Invalid email or password")

    return {"token": generate_token(user["id"]), "user": public_user(user)}


def authenticate_token(token):
    user_id = decode_token(token)
    if user_id is None:
        raise AuthenticationError("Invalid or expired token")

    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise AuthenticationError("User no longer exists")
    return user
