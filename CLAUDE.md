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

The analytics platform tracks traffic on a React/GitHub Pages portfolio site.
The deployment target is a Raspberry Pi 2 Model B v1.1 with 1 GB RAM, running
headless Raspberry Pi OS Lite (32-bit). Its architecture has been confirmed as
`armv7l` (Docker platform `linux/arm/v7`). Ethernet remains preferred, with a
working Ralink RT5370 USB WiFi adapter as an alternate connection. A dated
hardware and network snapshot is recorded in
`docs/project-details-2026-08-15.md`; transient values in it may be stale. The
Realtek adapter failure recorded there is historical. Offen image compatibility
has been validated; runtime resource use and persistence still need testing.

---

## Intended Architecture

The analytics server is not custom-built software. It runs Offen Fair Web
Analytics with SQLite in Docker Compose. This replaces the earlier local Umami
and PostgreSQL proof of concept because Umami does not publish an ARMv7 image.

Target stack:
- Offen Fair Web Analytics `v1.4.2`, pinned to a release with an ARMv7 image
- SQLite in a named Docker volume for persistent storage
- Docker Compose for service orchestration
- GitHub Actions for CI/CD: push to `main` triggers automated deploy to the Linux server
- Secure HTTPS ingress (Offen AutoTLS or a privacy-aware proxy; not yet selected)
- Analytics tracking embedded in the React/GitHub Pages portfolio site

Target deployment flow: `developer machine → GitHub → GitHub Actions → SSH → Raspberry Pi → service`

Automation is intentionally deferred until the learner can deploy, inspect,
back up, restore, and troubleshoot the service manually.

---

## Collaboration Style

The user's primary goal for this project is **hands-on learning**. Default to discussion, explanation, and guidance — not writing code.

- **Do not write code unless explicitly asked.** ("Write this for me", "generate the config", "code this up", etc.)
- When the next step involves writing something, explain what needs to be written and why, then let the user write it.
- If the user is stuck or asks for a hint, give targeted guidance rather than the full solution.
- Brainstorming, tradeoff discussion, and concept explanations are always appropriate.

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
