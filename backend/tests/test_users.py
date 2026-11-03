def test_me_returns_current_user(client, auth_headers):
    response = client.get("/api/users/me", headers=auth_headers)
    assert response.status_code == 200
    assert response.get_json()["data"]["email"] == "harit@example.com"


def test_list_users(client, auth_headers):
    response = client.get("/api/users/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.get_json()["data"]) == 1


def test_get_missing_user_is_404(client, auth_headers):
    response = client.get("/api/users/999", headers=auth_headers)
    assert response.status_code == 404
