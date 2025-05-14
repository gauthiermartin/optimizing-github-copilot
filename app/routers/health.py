"""
Health check endpoints for the application.

This module provides a health endpoint that returns status information
about the API's availability.
"""

import platform
import time
from typing import Any, Dict

from fastapi import APIRouter, status

router = APIRouter(
    prefix="/health",
    tags=["Health"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    response_description="Health status information",
)
async def health_check() -> Dict[str, Any]:
    """
    Perform a health check of the service.

    Returns:
        A dictionary containing:
        - status: The current status of the API (ok)
        - timestamp: The current timestamp
        - version: Python version information
        - uptime: System uptime information
    """
    return {
        "status": "ok",
        "timestamp": time.time(),
        "python_version": platform.python_version(),
        "system": platform.system(),
    }
