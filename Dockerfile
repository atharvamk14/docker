# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install NumPy
RUN pip install numpy

# Command to run on container start
CMD ["python", "./matrix_multiplication.py"]
