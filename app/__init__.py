import os

from flask import Flask

from .models import db
from ..config import get_config


def create_app():
    app = Flask(__name__)

    # Get the environment name from the environment variable, default to 'development'
    env_name = os.environ.get("FLASK_ENV", "development")
    app.config.from_object(get_config(env_name))

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Import and register the API blueprint
    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route("/favicon.ico")
    def favicon():
        return "", 204

    return app
