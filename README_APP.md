# FastAPI Health Application

A simple FastAPI application with a health endpoint, following best practices for project structure, testing, and dependency management.

## Features

- Health endpoint for monitoring application status
- Structured according to FastAPI best practices
- Type hints and comprehensive docstrings
- Testing with pytest
- Modern dependency management with uv
- Docker support

## Project Structure

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
tests/
├── conftest.py
└── test_health.py
```

## Installation

### Using uv (recommended)

1. Install uv (if not already installed)
   ```bash
   pip install uv
   ```

2. Install dependencies
   ```bash
   uv sync
   ```

### Using pip

```bash
pip install -e .
```

## Running the Application

### Development Mode

```bash
uv run -m uvicorn app.main:app --reload
```

or

```bash
python -m main
```

### Production Mode

```bash
uv run -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the application is running, access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Health Endpoint

The `/health` endpoint provides basic status information:

```json
{
  "status": "ok",
  "timestamp": 1621523456.789,
  "python_version": "3.12.0",
  "system": "Darwin"
}
```

## Running Tests

```bash
uv run -m pytest
```

Run tests with coverage:

```bash
uv run -m pytest --cov=app tests/ --cov-report term-missing
```

## Docker

Build the Docker image:

```bash
docker build -t fastapi-health-app .
```

Run the container:

```bash
docker run -p 8000:8000 fastapi-health-app
```

Or using docker-compose:

```bash
docker-compose up --build
```

## Validation Checklist

- Health endpoint returns 200 OK with appropriate status information
- Swagger documentation is accessible and correctly displays API endpoints
- Tests pass with no failures or errors
- Application starts without errors in both local and Docker environments
