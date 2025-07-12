# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
# This file should contain:
# functions-framework
# google-cloud-firestore
COPY requirements.txt ./

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the function code into the container
# This assumes your function code is in a file named 'main.py'
COPY main.py ./

# The Cloud Functions runtime expects the function to be served by functions-framework.
# We specify the target function name 'submit_feedback' and the port.
# For local testing, you can map this port. When deployed to Cloud Run/Functions,
# Google Cloud handles the port mapping.
CMD ["functions-framework", "--target", "submit_feedback", "--port", "8080"]

# Expose the port the function will listen on
EXPOSE 8080
