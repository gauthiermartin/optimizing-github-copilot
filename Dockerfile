FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project requirements
COPY pyproject.toml .

# Install dependencies using uv for reproducible builds
RUN uv pip install --system .

# Copy the rest of the application
COPY . .

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
