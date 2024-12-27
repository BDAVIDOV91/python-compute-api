import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import logging

db = SQLAlchemy()


def create_app():
    # Load environment variables
    load_dotenv()

    # Create Flask app
    app = Flask(
        __name__,
        instance_path=os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "../instance"
        ),
    )

    # Configure app
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///instance/app.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Using database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    logging.info(f"Database path: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    # Ensure instance directory exists
    instance_dir = os.path.join(os.getcwd(), "instance")
    if not os.path.exists(instance_dir):
        logging.info(f"Creating instance directory at {instance_dir}")
        os.makedirs(instance_dir)
    else:
        logging.info(f"Instance directory exists at {instance_dir}")

    # Initialize database
    db.init_app(app)
    with app.app_context():
        try:
            db.create_all()
            logging.info("Database tables created successfully")
        except Exception as e:
            logging.error(f"Error creating database tables: {e}")
            logging.error(f"Exception details: {e.__class__.__name__}: {e}")

    # Register blueprints
    from app.api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route("/favicon.ico")
    def favicon():
        return "", 204

    return app
