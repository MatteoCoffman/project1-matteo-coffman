# Use the official Python base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8080

# Start the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "-w", "4", "app:app"]
