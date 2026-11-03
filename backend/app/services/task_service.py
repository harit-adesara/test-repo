from app.errors import NotFoundError, PermissionDenied
from app.repositories import task_repository
from app.utils.pagination import get_offset, total_pages
from app.utils.validators import validate_status, validate_title


def create_task(user_id, title, description="", status="todo"):
    title = validate_title(title)
    status = validate_status(status)
    return task_repository.create_task(user_id, title, description or "", status)


def get_task(user_id, task_id):
    task = task_repository.get_task_by_id(task_id)
    if not task:
        raise NotFoundError("Task not found")
    if task["user_id"] != user_id:
        raise PermissionDenied("You do not own this task")
    return task


def list_tasks(user_id, page, per_page, status=None):
    if status:
        validate_status(status)

    offset = get_offset(page, per_page)
    items = task_repository.list_tasks_for_user(
        user_id, status=status, limit=per_page, offset=offset
    )
    total = task_repository.count_tasks_for_user(user_id, status=status)
    return {
        "items": items,
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages(total, per_page),
    }


def update_task(user_id, task_id, payload):
    get_task(user_id, task_id)  # ownership + existence check

    fields = {}
    if "title" in payload:
        fields["title"] = validate_title(payload["title"])
    if "description" in payload:
        fields["description"] = payload["description"] or ""
    if "status" in payload:
        fields["status"] = validate_status(payload["status"])
    return task_repository.update_task(task_id, fields)


def delete_task(user_id, task_id):
    get_task(user_id, task_id)
    task_repository.delete_task(task_id)
