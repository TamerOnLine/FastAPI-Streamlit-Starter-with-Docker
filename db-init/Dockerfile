# Use a specific PostgreSQL image version
FROM postgres:15

# Set environment variables (use default if not provided)
ENV POSTGRES_USER=${POSTGRES_USER:-default_user}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-default_password}
ENV POSTGRES_DB=${POSTGRES_DB:-default_db}


# Copy SQL initialization script
COPY . /docker-entrypoint-initdb.d/

# Add secure authentication to pg_hba.conf
RUN echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf

# Expose PostgreSQL port
EXPOSE 5432

# Run PostgreSQL
CMD ["postgres"]
