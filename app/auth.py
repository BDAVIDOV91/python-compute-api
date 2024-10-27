from flask import request

PASS_PHRASE = "mypass123"


def authorize(req):
    # Check if the 'Authorization' header is present
    auth_header = req.headers.get("Authorization")

    if auth_header is None:
        return False

    return auth_header == PASS_PHRASE
