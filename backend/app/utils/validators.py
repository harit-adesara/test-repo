import re

from app.errors import ValidationError

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
VALID_STATUSES = ("todo", "in_progress", "done")


def validate_email(email):
    if not isinstance(email, str) or not EMAIL_PATTERN.match(email.strip()):
        raise ValidationError("A valid email address is required")
    return email.strip().lower()


def validate_password(password):
    if not isinstance(password, str) or len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")
    if password.isalpha() or password.isdigit():
        raise ValidationError("Password must mix letters and numbers")
    return password


def validate_name(name):
    if not isinstance(name, str) or not name.strip():
        raise ValidationError("Name is required")
    return name.strip()


def validate_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValidationError("Task title is required")
    if len(title.strip()) > 120:
        raise ValidationError("Task title must be 120 characters or fewer")
    return title.strip()


def validate_status(status):
    if status not in VALID_STATUSES:
        raise ValidationError(
            "Status must be one of: " + ", ".join(VALID_STATUSES)
        )
    return status
