# Analytics Server

Learning-first, self-hosted web analytics for my [portfolio site](https://james-dyer.github.io/portfolio-website/), targeting a Raspberry Pi 2 Linux server.

## Overview

This repository deploys [Offen Fair Web Analytics](https://www.offen.dev/) to a
Raspberry Pi 2. Offen was selected after the Pi was confirmed to use 32-bit
ARMv7 and the Umami image was found not to publish an ARMv7 build.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for the staged learning plan and
[`docs/FIRST-BOOT.md`](docs/FIRST-BOOT.md) for the first hands-on session.
The dated [`docs/project-details-2026-08-15.md`](docs/project-details-2026-08-15.md)
snapshot records the observed Pi hardware, OS, storage, access, and network state;
its transient values may now be stale.

## Stack

- **[Offen](https://www.offen.dev/)** — privacy-focused, open-source analytics
- **SQLite** — lightweight persistent event storage
- **Docker Compose** — service orchestration
- **Raspberry Pi OS Lite** — intended headless host operating system
- **GitHub Actions** — later CI/CD milestone
- **HTTPS ingress** — Offen AutoTLS or a privacy-aware proxy, selected later

## Local Development

Requires Docker and a `.env` file containing an Offen application secret:

```dotenv
OFFEN_SECRET=replace-with-a-generated-secret
```

Generate the value with `docker run --rm offen/offen:v1.4.2 secret -quiet`. Do not
commit the resulting `.env` file or paste the secret into chat or terminal
transcripts.

Create the first account before starting the service. The command prompts for
the account password without displaying it:

```bash
docker compose run --rm offen setup -email YOUR_EMAIL -name YOUR_SITE
```

```bash
docker compose up -d    # Start all services
docker compose down     # Stop all services
docker compose logs -f  # Tail logs
docker compose ps       # Check container status
```

Offen will be available at `http://localhost:3000`. Its built-in health endpoint
is `http://localhost:3000/healthz`.

## Current boundary

Do not expose port 3000 or SSH to the public internet yet. The current Compose
file binds Offen to all host interfaces for LAN testing. Do not forward that
port through the router; public collection requires a separately designed HTTPS
ingress configuration.
