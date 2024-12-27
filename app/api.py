from flask import Blueprint, request, jsonify
from app.auth import authorize, generate_token
from app.calculate import process_csv
from app.models import Request, Result, db
import logging

api_bp = Blueprint("api", __name__)


@api_bp.route("/compute", methods=["POST"])
@authorize
def compute():
    if "file" not in request.files:
        logging.error("No file provided in the request.")
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    user = request.user
    filename = file.filename

    try:
        result_value = process_csv(file)

        new_request = Request(user=user, filename=filename)
        db.session.add(new_request)
        db.session.commit()

        new_result = Result(request_id=new_request.id, result=result_value)
        db.session.add(new_result)
        db.session.commit()

        logging.info(f"Successfully processed file: {filename} for user: {user}")
        return (
            jsonify({"message": "File processed successfully", "result": result_value}),
            200,
        )

    except Exception as e:
        logging.error(f"Error processing file: {filename} for user: {user} - {str(e)}")
        return jsonify({"error": "Failed to process file"}), 500
