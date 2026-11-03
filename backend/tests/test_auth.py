def register(client, **overrides):
    payload = {"name": "Rahul", "email": "rahul@example.com", "password": "secret123"}
    payload.update(overrides)
    return client.post("/api/auth/register", json=payload)


def test_register_success(client):
    response = register(client)
    assert response.status_code == 201
    data = response.get_json()["data"]
    assert data["email"] == "rahul@example.com"
    assert "password_hash" not in data


def test_register_duplicate_email(client):
    register(client)
    response = register(client)
    assert response.status_code == 409


def test_register_weak_password(client):
    response = register(client, password="short")
    assert response.status_code == 422


def test_login_success(client):
    register(client)
    response = client.post(
        "/api/auth/login",
        json={"email": "rahul@example.com", "password": "secret123"},
    )
    assert response.status_code == 200
    assert response.get_json()["data"]["token"]


def test_login_wrong_password(client):
    register(client)
    response = client.post(
        "/api/auth/login",
        json={"email": "rahul@example.com", "password": "wrongpass1"},
    )
    assert response.status_code == 401


def test_protected_route_requires_token(client):
    response = client.get("/api/users/me")
    assert response.status_code == 401
