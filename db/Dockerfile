FROM postgres:latest

# Declare build arguments for non-sensitive data
ARG POSTGRES_USER=postgres
ARG POSTGRES_DB=postgres

# Set environment variables for PostgreSQL (exclude sensitive data)
ENV POSTGRES_USER=$POSTGRES_USER \
    POSTGRES_DB=$POSTGRES_DB

# Copy SQL initialization script
COPY ../init.sql /docker-entrypoint-initdb.d/

# Expose PostgreSQL default port
EXPOSE 5432
