from app.logger import get_logger
from app.utils.responses import error_response

logger = get_logger(__name__)


class AppError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        if status_code is not None:
            self.status_code = status_code


class ValidationError(AppError):
    status_code = 422


class AuthenticationError(AppError):
    status_code = 401


class PermissionDenied(AppError):
    status_code = 403


class NotFoundError(AppError):
    status_code = 404


class ConflictError(AppError):
    status_code = 409


def register_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(exc):
        return error_response(exc.message, exc.status_code)

    @app.errorhandler(404)
    def handle_404(_exc):
        return error_response("Resource not found", 404)

    @app.errorhandler(405)
    def handle_405(_exc):
        return error_response("Method not allowed", 405)

    @app.errorhandler(Exception)
    def handle_unexpected(exc):
        logger.exception("Unhandled error: %s", exc)
        return error_response("Internal server error", 500)
