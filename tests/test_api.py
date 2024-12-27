from io import BytesIO
import pytest
from app import create_app
from app.auth import generate_token
from app.models import db  # Import the db object
import logging


@pytest.fixture
def test_client():
    app = create_app()
    app.config.from_object("config.TestingConfig")  # Use the testing configuration
    app.testing = True

    logging.info(f"Using database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables in the in-memory database
        yield client


@pytest.fixture
def auth_header():
    user = "test_user"
    token = generate_token(user)
    return {"Authorization": f"Bearer {token}"}


def test_compute_endpoint(test_client, auth_header):
    """Test the /compute endpoint."""
    csv_data = b"A,O,B\n1,2,3\n4,5,6\n"  # Use bytes
    data = {"file": (BytesIO(csv_data), "test.csv")}  # Use BytesIO

    response = test_client.post(
        "/api/compute",  # Ensure to use the correct path
        data=data,
        content_type="multipart/form-data",
        headers=auth_header,  # Use the JWT token in the authorization header
    )

    assert response.status_code == 200  # Check for successful response


def test_compute_endpoint_no_file(test_client, auth_header):
    """Test the /compute endpoint with no file provided."""
    response = test_client.post(
        "/api/compute",
        headers=auth_header,  # Add the authorization header
    )
    assert response.status_code == 400  # Check for bad request response


def test_compute_endpoint_invalid_token(test_client):
    """Test the /compute endpoint with an invalid token."""
    csv_data = b"A,O,B\n1,2,3\n4,5,6\n"
    data = {"file": (BytesIO(csv_data), "test.csv")}

    response = test_client.post(
        "/api/compute",
        data=data,
        content_type="multipart/form-data",
        headers={"Authorization": "Bearer invalid_token"},  # Use an invalid token
    )

    assert response.status_code == 401
