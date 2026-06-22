# Analytics Server

Self-hosted web analytics for my [portfolio site](https://james-dyer.github.io/portfolio-website/), deployed to a personal Linux server via Docker Compose and GitHub Actions.

## Overview

This repository contains the infrastructure configuration for a self-hosted [Umami](https://umami.is/) analytics instance.  The deployment target is a personal Linux server running Docker, with automated deploys triggered on push to `main`.

## Stack

- **[Umami](https://umami.is/)** — open-source analytics
- **PostgreSQL** — persistent event storage
- **Docker Compose** — service orchestration
- **GitHub Actions** — CI/CD pipeline
- **Reverse proxy** — external access (in progress)

## Local Development

Requires Docker and a `.env` file with the following variables:

```
POSTGRES_USER=
POSTGRES_PASSWORD=
APP_SECRET=
```

```bash
docker compose up -d    # Start all services
docker compose down     # Stop all services
docker compose logs -f  # Tail logs
docker compose ps       # Check container status
```

Umami will be available at `http://localhost:3000`.

## Deployment

Pushing to `main` triggers a GitHub Actions workflow that SSHs into the Linux server and runs `docker compose pull && docker compose up -d`. Deployment pipeline is currently in progress.
