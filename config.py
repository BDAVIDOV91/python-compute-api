# config.py still in progress

import os


class Config:
    """Configuration settings for the Flask application.
    This class is currently a work in progress.
    Additional settings will be added to ensure proper configuration
    for database, logging, and other application-specific settings.
    """

    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_very_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False
