# Analytics Server — Project Overview

## Rules:

Only update when goals, scope, architecture, or requirements change.
Never update because you completed work.
Treat it like a product requirements document (PRD).
Serves as the long-term source of truth.

---

# Purpose

This project is an infrastructure and DevOps learning environment. It self-hosts an analytics platform on a personal Linux server to develop hands-on experience with Linux administration, Docker, CI/CD, and self-hosting.

It also serves a practical purpose: tracking traffic on the portfolio website to understand recruiter engagement.

---

# Hardware and Hosting Environment

## Deployment Machine

The deployment target is a Raspberry Pi 2 Model B v1.1 with 1 GB of RAM. The
2026-08-15 inspection recorded Raspberry Pi OS Lite (32-bit); subsequent
inspection confirmed `armv7l`, corresponding to Docker platform `linux/arm/v7`.

Ethernet is the preferred home-network connection. A Ralink RT5370 USB WiFi
adapter also connects successfully and provides a secondary LAN path. The
Realtek RTL8188CUS failure recorded in
`docs/project-details-2026-08-15.md` is a historical observation. Addresses,
versions, storage figures, and network state in that dated snapshot may be stale.

The server will run headlessly and remain powered on continuously. Raspberry
Pi OS Lite is the preferred starting operating system because this project does
not need a desktop environment.

## Development Environment

Development will primarily occur on the main laptop.

The Raspberry Pi should be treated as a deployment target rather than the
primary development machine.

---

# Analytics Server

## Learning Goals

* Linux administration
* Docker and Docker Compose, if supported by the chosen analytics stack on the
  Pi's architecture
* Containerized deployments and self-hosting
* GitHub Actions CI/CD
* HTTPS and reverse proxy concepts
* Environment and secrets management

---

## Website Context

Portfolio website:

https://james-dyer.github.io/portfolio-website/

Current stack:

* React
* GitHub Pages

Expected traffic:

* Very low traffic
* Likely under 100 visits per month

---

## Analytics Goals

The analytics system should help answer:

* Are recruiters visiting the portfolio?
* Which pages receive the most attention?
* What content appears most interesting?
* What paths do visitors follow?
* Where do visitors leave?
* What improvements should be made to the portfolio?

---

## Implementation Approach

Use Offen Fair Web Analytics with SQLite rather than building a custom analytics
solution. The official `offen/offen:v1.4.2` image publishes an ARMv7 variant;
the earlier Umami proof of concept was rejected because its image does not.
Runtime memory use and persistence must still be validated on the Pi 2.

Required characteristics:

* Self-hosted
* Reproducible deployment (prefer Docker if hardware-compatible)
* Persistent storage
* Lightweight
* Low maintenance

---

## Repository Strategy

This project should have its own repository.

Reasons:

* Independent lifecycle
* Lower complexity
* Easier CI/CD experimentation
* Infrastructure learning environment

---

## Infrastructure Learning Goals

The analytics project should establish experience with:

* Linux server setup
* SSH
* Docker
* Docker Compose
* GitHub Actions
* Automated deployment
* Environment management
* HTTPS ingress and reverse proxy concepts
* Domain and networking concepts

---

# Development Workflow

## Source Control

GitHub is the source of truth for this repository.

---

## Containerization

Docker Compose orchestrates a single pinned Offen container. SQLite data is
stored in a named volume. The deployment must operate reliably within the Pi's
1 GB memory limit and survive both container and device restarts.

---

## CI/CD

A lightweight CI/CD pipeline is preferred.

Potential workflow:

Developer Machine
↓
GitHub
↓
GitHub Actions
↓
Linux Deployment Server
↓
Docker Deployment

Potential CI responsibilities:

* Linting
* Unit tests
* Build validation
* Docker image generation

Potential CD responsibilities:

* Automated deployment
* Service restart
* Health checks

---

# MVP Success Criteria

A successful MVP should:

* Run on the Linux server
* Collect portfolio page views in a persistent data store
* Survive a process restart and a device reboot
* Be accessible securely over HTTPS
* Track live traffic from the portfolio website

Automated deployment is a later milestone, after a manual deployment is fully
understood and repeatable.
