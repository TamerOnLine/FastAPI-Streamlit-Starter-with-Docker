# Variables
DOCKER_IMAGE_NAME = postgres-db
DOCKER_CONTAINER_NAME = my-postgres-db
DOCKER_BUILD_CONTEXT = .
PYTHON_MAIN_FILE = connection.py

# Build Docker image
build:
	docker-compose build

# Run services
up:
	docker-compose up -d

# Stop services
down:
	docker-compose down

# View logs
logs:
	docker-compose logs -f db

# Install Python dependencies
install-deps:
	pip install -r requirements.txt

# Run Python script
run-script:
	python $(PYTHON_MAIN_FILE)

# Cleanup Docker
clean:
	docker system prune -f
	docker volume prune -f

.PHONY: build up down logs install-deps run-script clean
