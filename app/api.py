import logging

from flask import Blueprint, jsonify, request

from .auth import authorize
from .calculate import process_csv
from .models import Request, Result, db

logging.basicConfig(level=logging.INFO)

api_bp = Blueprint("api", __name__)


@api_bp.route("/compute", methods=["POST"])
def compute():
    # Authorization
    if not authorize(request):
        logging.error("Unauthorized access attempt.")
        return jsonify({"error": "Unauthorized"}), 401

    # Check if a file is provided
    if "file" not in request.files:
        logging.error("No file provided in the request.")
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    user = "Anonymous"  # Replace with actual user info if available
    filename = file.filename
    request_name = "Request for " + filename  # Dynamically generated request name

    # Process the CSV file and perform calculations
    try:
        result_value = process_csv(file)  # Ensure this returns a numeric value

        # Save request and result in the database
        new_request = Request(user=user, request_name=request_name, filename=filename)
        db.session.add(new_request)
        db.session.commit()  # Save the request to get the request_id

        new_result = Result(request_id=new_request.id, result=result_value)
        db.session.add(new_result)
        db.session.commit()  # Save the result

        logging.info(f"Successfully processed file: {filename} for user: {user}")
        return jsonify({"result": result_value}), 200

    except ValueError as ve:
        logging.error(f"CSV parsing error: {ve}")
        db.session.rollback()
        return jsonify({"error": "Invalid CSV format or data"}), 400

    except db.IntegrityError as ie:
        logging.error(f"Database integrity error: {ie}")
        db.session.rollback()
        return jsonify({"error": "Database error while saving request"}), 500

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        db.session.rollback()
        return jsonify({"error": "An unexpected error occurred"}), 500
