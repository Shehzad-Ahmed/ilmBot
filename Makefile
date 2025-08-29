# Variables
DOCKER_IMAGE_NAME = ilmbot-api

# Default target
.PHONY: help
help:
	@echo "Choose a make command:"
	@echo "  install        - Install all dependencies using Poetry"
	@echo "  build          - Build the Docker images"
	@echo "  run            - Run the Docker containers"
	@echo "  stop           - Stop the Docker containers"
	@echo "  test           - Run tests using pytest inside Docker"

# Install dependencies
.PHONY: install
install:
	poetry install
	poetry run pre-commit install

# Build the Docker image
.PHONY: build
build:
	docker compose build --no-cache

# Run the Docker containers
.PHONY: run
run:
	docker compose up -d

# Stop the Docker containers
.PHONY: stop
stop:
	docker compose stop

# Run tests using pytest inside Docker
.PHONY: test
test:
	docker compose run --rm $(DOCKER_IMAGE_NAME) poetry run pytest $(ARGS)
