"""
Core application configuration.

This module contains settings, environment variable handling, and logging configuration
for the FastAPI application.
"""

import logging
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Attributes:
        app_name: The name of the application.
        debug: Debug mode flag.
        log_level: Logging level.
    """

    app_name: str = "FastAPI Health Application"
    debug: bool = False
    log_level: str = "INFO"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache()
def get_settings() -> Settings:
    """
    Get application settings from environment variables.

    Returns:
        Settings object with application configuration.
    """
    return Settings()


def configure_logging() -> None:
    """Configure application logging based on settings."""
    settings = get_settings()

    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Reduce level of some chatty libraries
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
