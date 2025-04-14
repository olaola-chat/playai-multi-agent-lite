# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy only dependency files first
COPY pyproject.toml poetry.lock ./
COPY .env .

# Configure poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies (with --no-root flag to skip installing the current project)
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Expose the port the app runs on
EXPOSE 18090

# Command to run the application using Gunicorn with Uvicorn workers
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:18090", "--timeout", "120", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]

