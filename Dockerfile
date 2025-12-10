# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy Python files and requirements
COPY requirements.txt .
COPY googletojson.py .
COPY main.py .
COPY start.sh .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make start.sh executable
RUN chmod +x start.sh

# Expose the API port
EXPOSE 5000

# Start the container using the start script
CMD ["./start.sh"]