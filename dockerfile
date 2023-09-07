# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY app/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables for MongoDB and Redis
ENV MONGO_HOST mongo
ENV REDIS_HOST redis

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "80"]
