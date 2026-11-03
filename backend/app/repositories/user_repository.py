from app.database import get_db


def create_user(name, email, password_hash):
    db = get_db()
    cursor = db.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        (name, email, password_hash),
    )
    db.commit()
    return get_user_by_id(cursor.lastrowid)


def get_user_by_id(user_id):
    row = get_db().execute(
        "SELECT * FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    return dict(row) if row else None


def get_user_by_email(email):
    row = get_db().execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()
    return dict(row) if row else None


def list_users():
    rows = get_db().execute("SELECT * FROM users ORDER BY id").fetchall()
    return [dict(row) for row in rows]
