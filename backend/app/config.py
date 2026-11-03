import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DATABASE_PATH = os.environ.get("DATABASE_PATH", "app.db")
    TOKEN_MAX_AGE_SECONDS = 3600
    DEFAULT_PER_PAGE = 10
    MAX_PER_PAGE = 50
    TESTING = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DATABASE_PATH = ":memory:"


CONFIGS = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": Config,
}


def get_config(name=None):
    return CONFIGS.get(name or "default", Config)
