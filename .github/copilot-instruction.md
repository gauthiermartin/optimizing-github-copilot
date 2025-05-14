# Steps to Scaffold a Simple FastAPI Application with Health Endpoint

Here are the steps I would take to scaffold a simple FastAPI application with a health endpoint, following best practices and the recommended folder structure from the FastAPI documentation:

1. **Create the basic folder structure**:
   ```
   app/
   ├── __init__.py
   ├── main.py
   ├── routers/
   │   ├── __init__.py
   │   └── health.py
   └── core/
       ├── __init__.py
       └── config.py
   ```

2. **Set up the core configuration module** (`app/core/config.py`):
   - Define application settings
   - Set up environment variables handling
   - Configure logging

3. **Create the health router** (`app/routers/health.py`):
   - Import APIRouter from FastAPI
   - Define a health endpoint that returns status information
   - Include proper typing and status codes
   - Add informative docstrings

4. **Implement the main application** (`app/main.py`):
   - Import and configure the FastAPI application
   - Include the health router
   - Add application metadata (title, description, version)
   - Set up any global middleware or dependencies

5. **Create entry point** (`main.py` in the root directory):
   - Import the FastAPI app
   - Configure server settings for running the application
   - Add a conditional for running the app directly with `uv run`

6. **Set up dependency management with uv**:
   - Initialize the project with `uv init --app` to create a `pyproject.toml`
   - Add FastAPI dependencies using `uv add fastapi --extra standard`
   - Define Python version requirements (e.g., requires-python = ">=3.12")
   - Add additional development dependencies with `uv add --dev pytest httpx pytest-mock`
   - Use `uv.lock` for reproducible dependency resolution
   - Configure .gitignore file
   - Create README.md with setup and usage instructions

7. **Set up testing structure**:
   - Create a tests directory
   - Add basic health endpoint tests

8. **Add Docker configuration**:
   - Create a Dockerfile that uses `uv` for dependency management:
     - Start from Python base image (e.g., `python:3.12-slim`)
     - Copy uv from the official image (`COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/`)
     - Use `uv sync --frozen --no-cache` for reproducible builds
     - Configure the container to run the FastAPI app
   - Create docker-compose.yml for local development

This approach follows the recommended FastAPI project structure with proper separation of concerns, making the application maintainable and scalable. The health endpoint serves as a simple way to verify the API is running correctly. Using `uv` for Python and dependency management provides faster installation times, more reliable dependency resolution, and a consistent development environment across all platforms.

## Running the Application with uv

To run the FastAPI application using `uv`:

1. **Initialize the project**:
   ```bash
   uv init --app
   ```

2. **Add FastAPI dependencies**:
   ```bash
   uv add fastapi --extra standard
   ```

3. **For development, add testing dependencies**:
   ```bash
   uv add --dev pytest httpx pytest-mock
   ```

4. **Run the application**:
   ```bash
   uv run -m uvicorn main:app --reload
   ```
   
   Or with the FastAPI CLI if installed:
   ```bash
   uv run fastapi dev
   ```

5. **For testing**:
   ```bash
   uv run -m pytest
   ```

Your `pyproject.toml` should look similar to this:

```toml
[project]
name = "fastapi-health-app"
version = "0.1.0"
description = "FastAPI application with health endpoint"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "httpx",
    "pytest-mock",
]
```