# Use the PostgreSQL base image
FROM postgres:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy database initialization scripts
COPY ./db-init /docker-entrypoint-initdb.d/

# Copy the requirements file
COPY ./requirements.txt /app/requirements.txt

# Install the required Python libraries
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Copy the remaining project files
COPY . /app

# Expose the default PostgreSQL port
EXPOSE 5432
