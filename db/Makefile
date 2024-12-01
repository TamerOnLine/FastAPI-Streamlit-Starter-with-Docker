build:
	docker build \
		--build-arg POSTGRES_USER=$(grep POSTGRES_USER ../.env | cut -d '=' -f2) \
		--build-arg POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD ../.env | cut -d '=' -f2) \
		--build-arg POSTGRES_DB=$(grep POSTGRES_DB ../.env | cut -d '=' -f2) \
		-t postgres:latest .

run:
	docker run -d \
		--name postgres_container \
		-e POSTGRES_USER=$(grep POSTGRES_USER ../.env | cut -d '=' -f2) \
		-e POSTGRES_PASSWORD=$(grep POSTGRES_PASSWORD ../.env | cut -d '=' -f2) \
		-e POSTGRES_DB=$(grep POSTGRES_DB ../.env | cut -d '=' -f2) \
		-p 5432:5432 \
		postgres:latest
