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

The deployment environment is an older gaming laptop from approximately 2021.

Known facts:

* Previously ran Windows
* Experienced performance issues near end of regular usage
* Will be wiped and converted to Linux
* Will remain powered on 24/7
* Will remain plugged in continuously
* Connected to home WiFi
* Internet connection is generally reliable

## Development Environment

Development will primarily occur on the main laptop.

The Linux laptop should be treated as a deployment target rather than the primary development machine.

---

# Analytics Server

## Learning Goals

* Linux administration
* Docker and Docker Compose
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

Use an existing open-source analytics platform rather than building a custom analytics solution.

Required characteristics:

* Self-hosted
* Dockerized
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

Docker Compose orchestrates all services. Benefits: reproducible environments, simplified deployment, and consistent infrastructure across dev and production.

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
* Self-host a Dockerized analytics platform via Docker Compose
* Deploy automatically via GitHub Actions on push to `main`
* Persist analytics data across container restarts
* Be accessible externally via a reverse proxy
* Track live traffic from the portfolio website
