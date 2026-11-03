import hashlib
import hmac
import os

from flask import current_app
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

ITERATIONS = 100_000


def hash_password(password):
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)
    return salt.hex() + "$" + digest.hex()


def verify_password(password, stored_hash):
    try:
        salt_hex, digest_hex = stored_hash.split("$")
    except ValueError:
        return False
    salt = bytes.fromhex(salt_hex)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)
    return hmac.compare_digest(digest.hex(), digest_hex)


def _serializer():
    return URLSafeTimedSerializer(current_app.config["SECRET_KEY"])


def generate_token(user_id):
    return _serializer().dumps({"user_id": user_id})


def decode_token(token):
    """Return the user id inside a token, or None if it is invalid/expired."""
    max_age = current_app.config["TOKEN_MAX_AGE_SECONDS"]
    try:
        payload = _serializer().loads(token, max_age=max_age)
    except (BadSignature, SignatureExpired):
        return None
    return payload.get("user_id")
