# config.py still in progress

import os


class Config:
    """Configuration settings for the Flask application."""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_very_secret_key"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "sqlite:///instance/app.db"
    )
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
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"  # Use a separate test database
    WTF_CSRF_ENABLED = False  # Disable CSRF protection for testing


class ProductionConfig(Config):
    """Development configuration."""

    DEBUG = True
    SQLALCHEMY_ECHO = True  # Log SQL queries for debugging


config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config(env):
    return config_by_name.get(env, DevelopmentConfig)()
