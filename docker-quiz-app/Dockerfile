# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install Flask
RUN pip install --no-cache-dir Flask

# Expose the port the Flask application listens on (default is 5000)
EXPOSE 5000

# Set environment variables (optional, but good practice)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Command to run the Flask application
CMD ["flask", "run"]
