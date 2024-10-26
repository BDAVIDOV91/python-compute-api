import logging

from flask import Blueprint, jsonify, request

from .auth import authorize
from .calculate import process_csv
from .models import Request, Result, db  # Import the models and db session

logging.basicConfig(level=logging.INFO)

api_bp = Blueprint("api", __name__)


@api_bp.route("/compute", methods=["POST"])
def compute():
    # Step 1: Authorization
    if not authorize(request):
        return jsonify({"error": "Unauthorized"}), 401

    # Step 2: Check if a file is provided
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    user = "Anonymous"  # Replace with actual user info if available
    filename = file.filename

    # Step 3: Process the CSV file and perform calculations
    try:
        result_value = process_csv(file)  # Ensure this returns a numeric value

        # Step 4: Save request and result in the database
        new_request = Request(user=user, filename=filename)
        db.session.add(new_request)
        db.session.commit()  # Save the request to get the request_id

        new_result = Result(request_id=new_request.id, result=result_value)
        db.session.add(new_result)
        db.session.commit()  # Save the result

        return jsonify({"result": result_value}), 200
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500
