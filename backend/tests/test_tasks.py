def create_task(client, headers, title, **extra):
    return client.post("/api/tasks/", json={"title": title, **extra}, headers=headers)


def test_create_task(client, auth_headers):
    response = create_task(client, auth_headers, "Write docs")
    assert response.status_code == 201
    assert response.get_json()["data"]["status"] == "todo"


def test_create_task_requires_title(client, auth_headers):
    response = create_task(client, auth_headers, "   ")
    assert response.status_code == 422


def test_get_task(client, auth_headers):
    task_id = create_task(client, auth_headers, "Read").get_json()["data"]["id"]
    response = client.get(f"/api/tasks/{task_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.get_json()["data"]["title"] == "Read"


def test_update_task_status(client, auth_headers):
    task_id = create_task(client, auth_headers, "Ship").get_json()["data"]["id"]
    response = client.patch(
        f"/api/tasks/{task_id}", json={"status": "done"}, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.get_json()["data"]["status"] == "done"


def test_update_task_invalid_status(client, auth_headers):
    task_id = create_task(client, auth_headers, "Ship").get_json()["data"]["id"]
    response = client.patch(
        f"/api/tasks/{task_id}", json={"status": "blocked"}, headers=auth_headers
    )
    assert response.status_code == 422


def test_delete_task(client, auth_headers):
    task_id = create_task(client, auth_headers, "Temp").get_json()["data"]["id"]
    assert client.delete(f"/api/tasks/{task_id}", headers=auth_headers).status_code == 200
    assert client.get(f"/api/tasks/{task_id}", headers=auth_headers).status_code == 404


def test_cannot_access_other_users_task(client, auth_headers):
    task_id = create_task(client, auth_headers, "Private").get_json()["data"]["id"]

    client.post(
        "/api/auth/register",
        json={"name": "Eve", "email": "eve@example.com", "password": "secret123"},
    )
    login = client.post(
        "/api/auth/login", json={"email": "eve@example.com", "password": "secret123"}
    )
    eve = {"Authorization": "Bearer " + login.get_json()["data"]["token"]}

    assert client.get(f"/api/tasks/{task_id}", headers=eve).status_code == 403


def test_pagination_first_page(client, auth_headers):
    for index in range(5):
        create_task(client, auth_headers, f"Task {index}")

    response = client.get("/api/tasks/?page=1&per_page=2", headers=auth_headers)
    data = response.get_json()["data"]

    assert [task["title"] for task in data["items"]] == ["Task 0", "Task 1"]
    assert data["total"] == 5
    assert data["total_pages"] == 3


def test_filter_by_status(client, auth_headers):
    create_task(client, auth_headers, "A", status="done")
    create_task(client, auth_headers, "B")

    response = client.get("/api/tasks/?status=done", headers=auth_headers)
    items = response.get_json()["data"]["items"]
    assert [task["title"] for task in items] == ["A"]
