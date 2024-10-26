# app/__init__.py
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py (optional, can be added later)
    # app.config.from_pyfile('config.py', silent=True)

    # Import the API blueprint and register it
    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
