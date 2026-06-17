# Hermes Agent with Docker

This repository contains a Docker setup for running the Hermes Agent.

## Prerequisites

- Docker (v20.10+)
- Docker Compose (v1.29+)
- Git

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/arafat33-1525-star/hermes.git
cd hermes
cp .env.example .env
```

### 2. Build and Run with Docker

#### Using Docker Compose (Recommended)

```bash
# Build the image
docker-compose build

# Start the service
docker-compose up -d

# View logs
docker-compose logs -f hermes

# Stop the service
docker-compose down
```

#### Using Docker directly

```bash
# Build the image
docker build -t hermes-agent:latest .

# Run the container
docker run -d \
  --name hermes-agent \
  -p 8000:8000 \
  -v $(pwd):/app \
  --env-file .env \
  hermes-agent:latest

# View logs
docker logs -f hermes-agent

# Stop the container
docker stop hermes-agent
```

## Project Structure

```
hermes/
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── .dockerignore           # Files to exclude from Docker build
├── .env.example            # Environment variables template
└── README.md              # This file
```

## Environment Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Edit `.env` with your settings:
- `AGENT_NAME`: Name of the agent
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `API_PORT`: Port for API server
- `MODEL_NAME`: Your model name
- `MODEL_API_KEY`: API key for the model
- And other custom configurations

## Docker Commands

### Build

```bash
docker-compose build --no-cache
```

### Start

```bash
docker-compose up -d
```

### Stop

```bash
docker-compose down
```

### View Logs

```bash
docker-compose logs -f hermes
```

### Execute Commands

```bash
docker-compose exec hermes python script.py
docker-compose exec hermes bash
```

### Remove Everything

```bash
docker-compose down -v
```

## Development

For development with live code reloading:

```bash
# The docker-compose.yml already mounts the local directory
docker-compose up -d

# Make changes to your code
# Changes will be reflected in the running container
```

## Production Deployment

For production, consider:

1. **Use specific Python version**: Replace `python:3.11-slim` with a specific version
2. **Multi-stage build**: Optimize image size
3. **Health checks**: Already included in Dockerfile
4. **Security**: Use secrets management instead of .env files
5. **Monitoring**: Add logging and monitoring solutions
6. **Reverse proxy**: Use nginx or similar

Example production Dockerfile:

```dockerfile
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .
CMD ["python", "-m", "hermes.agent"]
```

## Troubleshooting

### Container won't start

```bash
# Check logs
docker-compose logs hermes

# Verify the image was built
docker images | grep hermes
```

### Port already in use

```bash
# Change port in docker-compose.yml or use different port
docker-compose down
# Edit docker-compose.yml to use different port
docker-compose up -d
```

### Permission issues

```bash
# If you have file permission issues
sudo chown -R $USER:$USER .
```

## References

- [Official Hermes Agent Repository](https://github.com/NousResearch/hermes-agent)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

## License

See LICENSE file for details.
