from flask import Blueprint, g, request

from app.errors import ValidationError
from app.middleware import login_required
from app.services import task_service
from app.utils.pagination import parse_pagination
from app.utils.responses import success_response

task_bp = Blueprint("tasks", __name__)


def _json_body():
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        raise ValidationError("Request body must be a JSON object")
    return body


@task_bp.post("/")
@login_required
def create():
    body = _json_body()
    task = task_service.create_task(
        g.current_user["id"],
        body.get("title"),
        body.get("description", ""),
        body.get("status", "todo"),
    )
    return success_response(task, 201)


@task_bp.get("/")
@login_required
def list_all():
    page, per_page = parse_pagination(request.args)
    result = task_service.list_tasks(
        g.current_user["id"], page, per_page, request.args.get("status")
    )
    return success_response(result)


@task_bp.get("/<int:task_id>")
@login_required
def get_one(task_id):
    return success_response(task_service.get_task(g.current_user["id"], task_id))


@task_bp.patch("/<int:task_id>")
@login_required
def update(task_id):
    task = task_service.update_task(g.current_user["id"], task_id, _json_body())
    return success_response(task)


@task_bp.delete("/<int:task_id>")
@login_required
def delete(task_id):
    task_service.delete_task(g.current_user["id"], task_id)
    return success_response({"deleted": True})
