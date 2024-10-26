import os

from flask import Flask

from .models import db  # Import db directly from models


def create_app():
    app = Flask(__name__)

    # Set the database URI (SQLite in this case) to the main app.db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        os.path.dirname(__file__), "app.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
        False  # Disable track modifications for performance
    )

    # Initialize the SQLAlchemy database with the app
    db.init_app(app)

    # Create tables within the app context
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    # Import and register the API blueprint
    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route("/favicon.ico")
    def favicon():
        return "", 204  # No content response for favicon requests

    return app
