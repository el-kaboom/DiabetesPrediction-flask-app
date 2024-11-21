# Dockerfile for Flask
FROM python:3.9-slim

WORKDIR /app

# Copy the requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask application into the container
COPY . /app/

# Expose the port Flask app will run on (default is 5000)
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
