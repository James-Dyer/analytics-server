# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Session Continuity Documents

Read both documents at the start of every session before doing any work.

### `Project-Overview.md` — PRD / source of truth
Defines project goals, scope, architecture, and requirements.
- **Only update** when goals, scope, architecture, or requirements change
- **Never update** because work was completed — completed work goes in `Progress.md`
- Treat it as a timeless product requirements document

### `Progress.md` — current state and open decisions
Tracks phase, status, open decisions, next steps, and TODOs.
- Update regularly as work progresses
- All temporary state, next steps, open questions, and status notes live here, not in `Project-Overview.md`

---

## Project Context

This repository self-hosts an open-source analytics platform on a personal Linux server. The primary purpose is hands-on learning: Linux administration, Docker, Docker Compose, GitHub Actions CI/CD, and reverse proxy configuration.

The analytics platform tracks traffic on a React/GitHub Pages portfolio site. The deployment target is an older gaming laptop (~2021) running Linux, always-on, connected via home WiFi.

---

## Intended Architecture

The analytics server is not custom-built software — it wraps an existing open-source analytics platform in Docker Compose with automated deployment.

Target stack:
- Self-hosted open-source analytics platform (not yet selected — see `Progress.md`)
- Docker Compose for service orchestration
- GitHub Actions for CI/CD: push to `main` triggers automated deploy to the Linux server
- Reverse proxy (not yet selected) for external access
- Analytics tracking embedded in the React/GitHub Pages portfolio site

Deployment flow: `developer machine → GitHub → GitHub Actions → SSH → Linux server → Docker Compose`

---

## Development Commands

```bash
# Once docker-compose.yml is configured:
docker compose up -d       # Start all services
docker compose down        # Stop all services
docker compose logs -f     # Tail service logs
docker compose pull        # Pull latest images
```

No application code exists yet; the Docker Compose configuration is the primary artifact to build.
