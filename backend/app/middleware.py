from functools import wraps

from flask import g, request

from app.errors import AuthenticationError
from app.services.auth_service import authenticate_token


def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            raise AuthenticationError("Missing bearer token")
        user = authenticate_token(header[len("Bearer "):])
        g.current_user = user
        return view(*args, **kwargs)

    return wrapper
