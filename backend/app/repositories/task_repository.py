from app.database import get_db


def create_task(user_id, title, description, status):
    db = get_db()
    cursor = db.execute(
        "INSERT INTO tasks (user_id, title, description, status) VALUES (?, ?, ?, ?)",
        (user_id, title, description, status),
    )
    db.commit()
    return get_task_by_id(cursor.lastrowid)


def get_task_by_id(task_id):
    row = get_db().execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    return dict(row) if row else None


def list_tasks_for_user(user_id, status=None, limit=10, offset=0):
    query = "SELECT * FROM tasks WHERE user_id = ?"
    params = [user_id]
    if status:
        query += " AND status = ?"
        params.append(status)
    query += " ORDER BY id LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    rows = get_db().execute(query, params).fetchall()
    return [dict(row) for row in rows]


def count_tasks_for_user(user_id, status=None):
    query = "SELECT COUNT(*) AS total FROM tasks WHERE user_id = ?"
    params = [user_id]
    if status:
        query += " AND status = ?"
        params.append(status)
    return get_db().execute(query, params).fetchone()["total"]


def update_task(task_id, fields):
    if not fields:
        return get_task_by_id(task_id)
    assignments = ", ".join(f"{column} = ?" for column in fields)
    db = get_db()
    db.execute(
        f"UPDATE tasks SET {assignments} WHERE id = ?",
        [*fields.values(), task_id],
    )
    db.commit()
    return get_task_by_id(task_id)


def delete_task(task_id):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
