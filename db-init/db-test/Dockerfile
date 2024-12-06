# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the default port (if the app requires one, مثل FastAPI أو Flask)
EXPOSE 8000

# Set ENTRYPOINT to Python
ENTRYPOINT ["python"]

# Define the command to run the application
CMD ["app.py"]
