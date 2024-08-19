# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install curl and other necessary packages
RUN apt-get update && apt-get install -y curl

# Install pipenv
RUN pip install pipenv

# Set environment variable to create virtual environment in the project directory
ENV PIPENV_VENV_IN_PROJECT=1

# Copy the Pipfile and Pipfile.lock into the container at /app
COPY . .

COPY Pipfile Pipfile.lock ./

RUN rm -rf .venv

# Install dependencies
RUN pipenv install 

# Expose the port the app runs on
EXPOSE 8000

# Run the application using gunicorn
CMD ["pipenv", "run", "gunicorn"]
