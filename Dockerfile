# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 for Uvicorn
EXPOSE $PORT

# Run the Flask app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "$PORT"]
