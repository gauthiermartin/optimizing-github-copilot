"""
FastAPI application main module.

This module initializes and configures the FastAPI application,
including routers, middleware, and application metadata.
"""

import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import configure_logging, get_settings
from app.routers.health import router as health_router

# Configure logging
configure_logging()
logger = logging.getLogger(__name__)

# Initialize settings
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle application lifespan events (startup and shutdown).

    This function is called when the application starts up, before it starts accepting
    requests, and when it shuts down, after it stops accepting requests. It's used to
    initialize and clean up resources that are shared across the application's lifetime.

    Code before the yield is executed during startup.
    Code after the yield is executed during shutdown.

    Args:
        app: FastAPI application instance.
    """
    # Startup event - initialize resources
    startup_time = time.time()
    logger.info(f"Starting {settings.app_name}")

    try:
        # Add any additional resource initialization here
        # For example: database connections, ML models, etc.

        # Signal successful startup
        logger.info(
            f"{settings.app_name} started successfully in "
            f"{time.time() - startup_time:.2f} seconds"
        )

        # Hand control back to the application
        yield
    except Exception as e:
        # Handle any exceptions during startup
        logger.error(f"Error during application startup: {e!s}")
        raise
    finally:
        # Shutdown event - clean up resources
        logger.info(f"Shutting down {settings.app_name}")
        # Add any resource cleanup code here
        # For example: closing database connections, etc.


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="A simple FastAPI application with a health endpoint",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    debug=settings.debug,
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers in the application
app.include_router(health_router)
