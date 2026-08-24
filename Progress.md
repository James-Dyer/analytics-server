# Progress

## Current Phase

The repository now implements a custom Flask/SQLAlchemy analytics service and
contains a production Gunicorn container intended for a 32-bit ARMv7 Raspberry
Pi 2. The production container is running on the Pi's LAN. Collection and
SQLite persistence have been verified locally, across a Pi container restart,
and across a full Pi reboot. Public ingress remains intentionally out of scope.

---

## Status

- ✅ Custom Flask application factory and health endpoint
- ✅ Validated page-view collection at `POST /events`
- ✅ SQLAlchemy event model with SQLite persistence
- ✅ Server-rendered dashboard at `GET /dashboard/`
- ✅ Unit and request tests for health, validation, persistence, and dashboard
- ✅ Production and development dependencies separated
- ✅ Gunicorn configured with one worker and two threads
- ✅ ARMv7-compatible Python 3.13 container base selected
- ✅ Container runs as a non-root user
- ✅ Compose uses a named volume for SQLite persistence
- ✅ Request bodies limited to 8 KiB
- ✅ Database health failures return HTTP 503
- ✅ Application and Gunicorn logs write to container stdout/stderr
- ✅ Production container built and exercised locally
- ✅ Container restart and replacement persistence verified locally
- ✅ ARMv7 image cross-built and health-checked under emulation
- ✅ Raspbian Docker 26.1.5 and Compose 2.26.1 installed on the Pi
- ✅ Service deployed and reachable from the development laptop over the LAN
- ✅ Persistence verified across container restart and full Pi reboot
- ✅ Pi measurements recorded: healthy within 35 seconds of observed startup;
  Gunicorn processes approximately 18 MiB and 35 MiB RSS; 714 MiB host memory
  available; 11 GB disk free; 48.2°C shortly after reboot
- ✅ Pi kernel limitation recorded: container memory limits/accounting unavailable
- ⬜ Firewall, DHCP reservation, and backups configured and documented
- ⬜ Exact-origin CORS and browser tracker implemented
- ⬜ Dashboard access restricted before public ingress
- ⬜ Secure HTTPS ingress configured
- ⬜ GitHub Actions deployment pipeline

---

## Open Decisions

### Infrastructure

- Whether a future OS/kernel should enable container memory accounting
- HTTPS ingress choice: privacy-aware reverse proxy or secure tunnel
- Whether to reserve the Ethernet address with DHCP
- Remote access strategy beyond LAN-only SSH
- Dashboard access method before public collection

### Analytics

- Bot/noise filtering policy after real traffic is observed
- Data retention period
- Seven- and thirty-day dashboard summaries and activity visualization

### CI/CD

Exact GitHub Actions pipeline implementation is intentionally deferred until the
manual deployment and rollback path are repeatable.

---

## Hardware Prep

The Pi was flashed and inspected on 2026-08-15. The dated snapshot records a
Raspberry Pi 2 Model B v1.1, 16 GB microSD card, 32-bit Raspberry Pi OS Lite,
working LAN SSH, and Ethernet as the preferred network connection. A replacement
Ralink RT5370 WiFi adapter also works. Addresses, package versions, storage use,
and current reachability may now be stale.

---

## Next Steps

1. Commit and push the LAN deployment implementation
2. Configure backups and perform a SQLite restore test
3. Decide how the dashboard will remain private before public collection
4. Add exact-origin CORS, rate limiting, and the browser tracker
5. Add HTTPS ingress only after those controls are ready
