import pytest

from app import create_app
from app.database import init_db


@pytest.fixture
def app(tmp_path):
    application = create_app("testing")
    # Use a real temp file so data survives across requests in one test.
    application.config["DATABASE_PATH"] = str(tmp_path / "test.db")
    with application.app_context():
        init_db()
    return application


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth_headers(client):
    client.post(
        "/api/auth/register",
        json={"name": "Harit", "email": "harit@example.com", "password": "secret123"},
    )
    response = client.post(
        "/api/auth/login",
        json={"email": "harit@example.com", "password": "secret123"},
    )
    token = response.get_json()["data"]["token"]
    return {"Authorization": f"Bearer {token}"}
