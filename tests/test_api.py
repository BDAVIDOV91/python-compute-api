# test_api.py is not fully working.It passes only 2 out of 3 tasks.

from io import BytesIO

import pytest

from app import create_app


@pytest.fixture
def test_client():
    app = create_app()
    app.testing = True

    with app.test_client() as client:
        yield client


def test_compute_endpoint(test_client):
    """Test the /compute endpoint."""
    csv_data = b"A,O,B\n1,2,3\n4,5,6\n"  # Use bytes
    data = {"file": (BytesIO(csv_data), "test.csv")}  # Use BytesIO

    response = test_client.post(
        "/api/compute",  # Ensure to use the correct path
        data=data,
        content_type="multipart/form-data",
        headers={"Authorization": "mypass123"},  # Add the authorization header
    )

    assert response.status_code == 200  # Check for successful response


def test_compute_endpoint_no_file(test_client):
    """Test the /compute endpoint with no file provided."""
    response = test_client.post(
        "/api/compute",
        headers={"Authorization": "mypass123"},  # Add the authorization header
    )
    assert response.status_code == 400  # Check for error when no file is provided


def test_compute_endpoint_unauthorized(test_client):
    """Test the /compute endpoint without authorization."""
    response = test_client.post("/api/compute", data={})  # No header
    assert response.status_code == 401  # Check for unauthorized response
