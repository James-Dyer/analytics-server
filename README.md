# Analytics Server

Learning-first, self-hosted web analytics for my [portfolio site](https://james-dyer.github.io/portfolio-website/), targeting a Raspberry Pi 2 Linux server.

## Overview

This repository contains an existing local proof of concept for a self-hosted [Umami](https://umami.is/) analytics instance. The next phase is to prepare a Raspberry Pi 2, validate its exact architecture and resource limits, and determine whether the current containers are a good fit.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for the staged learning plan and
[`docs/FIRST-BOOT.md`](docs/FIRST-BOOT.md) for the first hands-on session.

## Stack

- **[Umami](https://umami.is/)** — open-source analytics
- **PostgreSQL** — persistent event storage
- **Docker Compose** — service orchestration
- **Raspberry Pi OS Lite** — intended headless host operating system
- **GitHub Actions** — later CI/CD milestone
- **Reverse proxy and HTTPS** — later secure-access milestone

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

## Current boundary

Do not expose port 3000 or SSH to the public internet yet. The current Compose
file is for local experimentation and has not been validated on the Pi 2.
