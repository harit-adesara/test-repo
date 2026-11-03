from flask import Blueprint, request

from app.errors import ValidationError
from app.services import auth_service
from app.utils.responses import success_response

auth_bp = Blueprint("auth", __name__)


def _json_body():
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        raise ValidationError("Request body must be a JSON object")
    return body


@auth_bp.post("/register")
def register():
    body = _json_body()
    user = auth_service.register_user(
        body.get("name"), body.get("email"), body.get("password")
    )
    return success_response(user, 201)


@auth_bp.post("/login")
def login():
    body = _json_body()
    result = auth_service.login_user(body.get("email"), body.get("password"))
    return success_response(result)
