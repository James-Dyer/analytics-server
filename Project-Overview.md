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
2026-08-15 inspection recorded Raspberry Pi OS Lite (32-bit) reporting an `arm`
architecture. Container-image compatibility must still be validated against the
actual host environment.

Ethernet is the preferred home-network connection. The Realtek RTL8188CUS USB
WiFi adapter is detected, but connection attempts failed because of an apparent
Protected Management Frames policy mismatch. See the dated
`docs/project-details-2026-08-15.md` snapshot for the observations; addresses,
versions, storage figures, and network state in that document may be stale.

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
* Reverse proxy configuration
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

Begin with the existing Umami proof of concept rather than building a custom
analytics solution. Treat Umami-on-Pi as a hypothesis until its current image,
database, memory usage, and CPU architecture are validated on the actual Pi 2.

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
* Reverse proxy configuration
* Domain and networking concepts

---

# Development Workflow

## Source Control

GitHub is the source of truth for this repository.

---

## Containerization

Docker Compose currently orchestrates Umami and PostgreSQL for local
development. It remains the preferred production approach only if both images
support the Pi's architecture and operate reliably within its memory limit.

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
