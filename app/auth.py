import os
import jwt
from flask import request, jsonify
from functools import wraps

SECRET_KEY = os.environ.get("SECRET_KEY") or "bgts"


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"error": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = data["user"]
        except Exception as e:
            return jsonify({"error": "Token is invalid!"}), 401

        return f(*args, **kwargs)

    return decorated_function


def generate_token(user):
    token = jwt.encode({"user": user}, SECRET_KEY, algorithm="HS256")
    return token
