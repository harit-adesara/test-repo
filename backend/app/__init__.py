from flask import Flask

from app import database
from app.config import get_config
from app.errors import register_error_handlers
from app.logger import get_logger
from app.routes import register_routes

logger = get_logger(__name__)


def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    database.init_app(app)
    register_routes(app)
    register_error_handlers(app)

    logger.info("Application created (env=%s)", config_name or "default")
    return app
