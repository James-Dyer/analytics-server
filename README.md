# Analytics Server

Learning-first, self-hosted analytics for the
[portfolio site](https://james-dyer.github.io/portfolio-website/), targeting a
32-bit ARMv7 Raspberry Pi 2.

## Stack

- Flask HTTP service and server-rendered dashboard
- SQLAlchemy ORM with SQLite persistence
- Gunicorn production WSGI server
- Docker Compose for repeatable deployment
- `python:3.13.15-slim-bookworm`, which publishes `linux/arm/v7`

The service accepts validated page-view events at `POST /events`, reports
application and database health at `GET /healthz`, and displays collected data
at `GET /dashboard/`.

## Local development

Create and activate a virtual environment, then install development
dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --requirement requirements-dev.txt
```

Run the development server:

```bash
flask --app analytics run --debug
```

Run the tests:

```bash
python -m pytest -q
```

The development database is stored at `instance/analytics.db` and is ignored by
Git.

## Production container

Build and start the Gunicorn service:

```bash
docker compose up --build -d
docker compose ps
docker compose logs -f analytics
```

Open `http://localhost:3000/dashboard/` or check health:

```bash
curl --fail http://localhost:3000/healthz
```

Send a local test event:

```bash
curl --request POST http://localhost:3000/events \
  --header 'Content-Type: application/json' \
  --data '{"event_type":"pageview","path":"/deployment-test","referrer_host":null,"session_id":"manual-test"}'
```

SQLite data is stored in the `analytics-data` Docker volume and survives
container replacement. See [the LAN deployment runbook](docs/LAN-DEPLOYMENT.md)
for deployment and persistence checks on the Pi.

## Current security boundary

This configuration is for LAN validation only. Port 3000 binds to all host
interfaces so another device on the LAN can test it. Do not forward this port
through the router. The dashboard has no authentication, HTTPS is not yet
configured, and browser-origin controls have not been added.
