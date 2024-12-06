# Create the network
network:
	docker network create app_network || true

# Build the PostgreSQL image
build-postgres:
	docker build -t postgres_secure ./db-init

# Build the Python application image
build-python:
	docker build -t python_app ./my_python_app

# Start containers
up:
	docker-compose up -d

# Stop containers
stop:
	docker-compose down

# Clean up containers, volumes, and network
clean:
	docker system prune -f
	docker volume rm postgres_data || true
	docker network rm app_network || true
