from flask import Blueprint, jsonify, request

from .auth import authorize
from .calculate import process_csv
from .db import (
    init_db,  # Ensure these functions are defined in db.py
    save_request,
    save_result,
)

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
        result = process_csv(file)

        # Step 4: Save request and result in the database
        request_id = save_request(user, filename)
        save_result(request_id, result)

        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
