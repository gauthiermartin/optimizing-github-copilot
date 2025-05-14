"""
Tests for the health endpoint.
"""

from fastapi import status


def test_health_endpoint(client):
    """
    Test that the health endpoint returns the expected status.

    Args:
        client: The test client fixture.
    """
    # When: Making a GET request to the health endpoint
    response = client.get("/health")

    # Then: The response should have a 200 status code
    assert response.status_code == status.HTTP_200_OK

    # And: The response should include the expected fields
    data = response.json()
    assert "status" in data
    assert data["status"] == "ok"
    assert "timestamp" in data
    assert "python_version" in data
    assert "system" in data


def test_health_endpoint_content_type(client):
    """
    Test that the health endpoint returns JSON content.

    Args:
        client: The test client fixture.
    """
    # When: Making a GET request to the health endpoint
    response = client.get("/health")

    # Then: The response should have the correct content type
    assert response.headers["content-type"] == "application/json"
