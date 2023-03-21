# Use the official Python image as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django app
COPY . /app/
