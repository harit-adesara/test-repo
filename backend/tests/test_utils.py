import pytest

from app.errors import ValidationError
from app.utils import validators
from app.utils.pagination import get_offset, total_pages


def test_validate_email_normalises_case():
    assert validators.validate_email("  Test@Example.COM ") == "test@example.com"


def test_validate_email_rejects_garbage():
    with pytest.raises(ValidationError):
        validators.validate_email("not-an-email")


def test_validate_password_requires_length():
    with pytest.raises(ValidationError):
        validators.validate_password("a1")


def test_validate_password_requires_mixed_characters():
    with pytest.raises(ValidationError):
        validators.validate_password("onlyletters")


def test_validate_status_rejects_unknown():
    with pytest.raises(ValidationError):
        validators.validate_status("blocked")


def test_validate_title_rejects_long_titles():
    with pytest.raises(ValidationError):
        validators.validate_title("x" * 121)


def test_total_pages_rounds_up():
    assert total_pages(5, 2) == 3
    assert total_pages(0, 2) == 0


def test_get_offset_first_page_is_zero():
    assert get_offset(1, 10) == 0
    assert get_offset(3, 10) == 20
