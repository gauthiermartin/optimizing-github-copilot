"""
Fixtures for testing the FastAPI application.
"""

import os
import sys

import pytest
from fastapi.testclient import TestClient

from app.main import app

# Print debug information
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")
print(f"App module path: {app.__module__}")


@pytest.fixture
def client() -> TestClient:
    """
    Fixture providing a FastAPI TestClient.

    Returns:
        A FastAPI TestClient instance configured to test the application.
    """
    return TestClient(app)
