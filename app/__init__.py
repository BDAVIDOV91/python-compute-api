from flask import Flask

from .db import init_db  # Import the init_db function


def create_app():
    app = Flask(__name__)

    # Load configuration from config.py (optional, can be added later)
    # app.config.from_pyfile('config.py', silent=True)

    # Initialize the database
    init_db()  # Call the function to create the database and tables

    # Import the API blueprint and register it
    from .api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route("/favicon.ico")
    def favicon():
        return "", 204  # No content response for favicon requests

    return app
