from flask import Blueprint, request, jsonify
import logging
from .auth import authorize, generate_token
from .calculate import process_csv
from .models import Request, Result, db

logging.basicConfig(level=logging.INFO)

api_bp = Blueprint("api", __name__)


@api_bp.route("/compute", methods=["POST"])
@authorize
def compute():
    # Check if a file is provided
    if "file" not in request.files:
        logging.error("No file provided in the request.")
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    user = request.user  # Get user from the JWT token
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
        return (
            jsonify({"message": "File processed successfully", "result": result_value}),
            200,
        )

    except Exception as e:
        logging.error(f"Error processing file: {filename} for user: {user} - {str(e)}")
        return jsonify({"error": "Failed to process file"}), 500
