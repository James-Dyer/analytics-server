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
headless Raspberry Pi OS Lite (32-bit) and currently using Ethernet. A dated
hardware and network snapshot is recorded in
`docs/project-details-2026-08-15.md`; transient values in it may be stale. The
USB WiFi adapter was detected but could not connect because of an apparent
Protected Management Frames policy mismatch. Production container compatibility
and resource use still need to be validated on the reported ARM environment.

---

## Intended Architecture

The analytics server is not initially custom-built software. The existing local
proof of concept wraps Umami and PostgreSQL in Docker Compose. Production use on
the Pi is conditional on architecture compatibility and measured resource use.

Target stack:
- Existing local Umami + PostgreSQL proof of concept
- Docker Compose for service orchestration if the Pi supports the images reliably
- GitHub Actions for CI/CD: push to `main` triggers automated deploy to the Linux server
- Reverse proxy (not yet selected) for external access
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
