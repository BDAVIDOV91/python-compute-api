import os
import csv
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import logging
from app.db import init_db  # Import the init_db function
from app.calculate import process_csv  # Import the process_csv function

db = SQLAlchemy()


def create_app():
    # Load environment variables
    load_dotenv()

    # Create Flask app
    app = Flask(
        __name__,
        instance_path=os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "instance"
        ),
    )

    # Configure app
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///app/instance/app.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Using database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    logging.info(f"Database path: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # Ensure instance directory exists
    instance_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "instance")
    if not os.path.exists(instance_dir):
        logging.info(f"Creating instance directory at {instance_dir}")
        os.makedirs(instance_dir)
    else:
        logging.info(f"Instance directory exists at {instance_dir}")

    # Initialize database
    db.init_app(app)
    with app.app_context():
        from app.models import Request, Result  # Ensure models are imported

        logging.info("Creating database tables...")
        try:
            init_db()  # Call the init_db function to create tables
            logging.info("Database tables created successfully")
        except Exception as e:
            logging.error(f"Error creating database tables: {e}")
            logging.error(f"Exception details: {e.__class__.__name__}: {e}")
            import traceback

            logging.error(traceback.format_exc())

    # Register blueprints
    from app.api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route("/")
    def index():
        return redirect(url_for("admin"))

    @app.route("/admin")
    def admin():
        from app.models import Request, Result

        requests = Request.query.all()
        results = Result.query.all()

        # Read calculation results from the data/test_calculations.csv file
        data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
        calculations = []
        filepath = os.path.join(data_dir, "test_calculations.csv")
        if os.path.exists(filepath):
            with open(filepath, newline="") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    calculations.append(row)

        # Process the CSV file to calculate the result
        calculation_result = None
        if os.path.exists(filepath):
            try:
                calculation_result = process_csv(filepath)
            except Exception as e:
                logging.error(f"Error processing CSV file: {e}")

        return render_template(
            "admin.html",
            requests=requests,
            results=results,
            calculations=calculations,
            calculation_result=calculation_result,
        )

    @app.route("/favicon.ico")
    def favicon():
        return "", 204

    return app
