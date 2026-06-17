.PHONY: help build up down logs shell test clean

help:
	@echo "Hermes Agent Docker Commands"
	@echo "============================"
	@echo "make build       - Build Docker image"
	@echo "make up          - Start services"
	@echo "make down        - Stop services"
	@echo "make logs        - View service logs"
	@echo "make shell       - Open shell in container"
	@echo "make test        - Run tests"
	@echo "make clean       - Remove containers and volumes"
	@echo "make restart     - Restart services"
	@echo "make ps          - Show running containers"

build:
	docker-compose build

up:
	docker-compose up -d
	@echo "Services started. Use 'make logs' to view logs"

down:
	docker-compose down

logs:
	docker-compose logs -f hermes

shell:
	docker-compose exec hermes bash

test:
	docker-compose exec hermes pytest -v

clean:
	docker-compose down -v
	docker system prune -f

restart:
	docker-compose restart

ps:
	docker-compose ps

install-deps:
	pip install -r requirements.txt

dev:
	docker-compose up -d
	@echo "Development environment started"
	@echo "Access at http://localhost:8000"

prod-build:
	docker build -t hermes-agent:prod -f Dockerfile.prod .