import os


class Config:
    """Configuration settings for the Flask application."""

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'instance/app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications
    LOG_LEVEL = os.environ.get("LOG_LEVEL") or "INFO"
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER") or "uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for file uploads


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True
    SQLALCHEMY_ECHO = True  # Enable SQL query logging


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.abspath('instance/app.db')}"
    WTF_CSRF_ENABLED = False  # Disable CSRF protection for testing


class ProductionConfig(Config):
    """Development configuration."""

    DEBUG = False
    SQLALCHEMY_ECHO = False  # Log SQL queries for debugging


config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config(env):
    return config_by_name.get(env, DevelopmentConfig)()
