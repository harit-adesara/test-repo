from app.routes.auth_routes import auth_bp
from app.routes.health_routes import health_bp
from app.routes.task_routes import task_bp
from app.routes.user_routes import user_bp


def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(task_bp, url_prefix="/api/tasks")
