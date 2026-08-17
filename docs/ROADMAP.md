# Learning Roadmap

This roadmap is ordered so each phase teaches and proves one layer before the
next one is added. The commands and configuration should be typed and explained
by the learner; the repository records decisions and repeatable procedures.

## Phase 0 — Understand the architecture change

Goal: explain the current request path, persistence, and why the original stack
was replaced.

- Compare the earlier Umami/PostgreSQL proof of concept with Offen/SQLite.
- Trace browser → tracking endpoint → Offen → SQLite.
- Explain ports, environment variables, volumes, health checks, and restarts.
- Record why Umami cannot be deployed here without an ARMv7 image.

Exit check: draw the request path and explain what data survives `docker compose down`.

## Phase 1 — Prepare the Raspberry Pi

Goal: boot a minimal Linux system and administer it from the development laptop.

- Inventory the Pi revision, power supply, microSD card, and USB WiFi adapter.
- Flash Raspberry Pi OS Lite with hostname, user, WiFi, and SSH preconfigured.
- Find the Pi on the LAN and connect with SSH.
- Update packages, set the timezone/hostname, and reboot safely.
- Set up SSH keys after password login works; then disable password SSH login.

Exit check: reconnect after a reboot without attaching a monitor or keyboard.

## Phase 2 — Learn the Linux host

Goal: understand the machine before installing an application stack.

- Files and navigation: `pwd`, `ls`, `cd`, `cp`, `mv`, `mkdir`.
- Users and permissions: `whoami`, `id`, ownership, mode bits, `sudo`.
- Processes and resources: `ps`, `top`, `free`, `df`, `du`.
- Networking: addresses, ports, DNS, LAN versus internet.
- Packages and services: APT, `systemctl`, and `journalctl`.
- Logs and troubleshooting: form a hypothesis, inspect evidence, change one thing.

Exit check: identify a running service, inspect its logs, stop it, and start it.

## Phase 3 — Validate the analytics architecture

Goal: validate the selected Offen/SQLite stack on 1 GB ARMv7 hardware.

- Record model, architecture, OS version, RAM, swap, and free storage.
- Confirm the pinned Offen image publishes `linux/arm/v7`.
- Run the stack only on the LAN and observe idle/startup RAM, CPU, and temperature.
- Test database persistence through container restart and full device reboot.
- Pin image versions before calling the deployment repeatable.

Decision gate: continue with Offen if it remains responsive and persistent on
the Pi. If it does not, record the measurements before considering a native
binary, different hardware, or a custom collector with explicit privacy and
data-retention requirements.

## Phase 4 — Make manual deployment reliable

Goal: deploy from written instructions without automation hiding the mechanics.

- Clone the repository onto the Pi.
- Create secrets locally on the Pi; never commit `.env`.
- Start, inspect, stop, update, and roll back the service manually.
- Write backup and restore procedures and actually perform one restore test.
- Add a `systemd` unit only if Compose restart policies are insufficient.

Exit check: rebuild the service from the repo plus a documented backup.

## Phase 5 — Publish securely

Goal: accept analytics events from an HTTPS portfolio without exposing admin tools.

- Choose a domain/subdomain and secure ingress approach.
- Choose between Offen AutoTLS and a privacy-aware reverse proxy, then obtain TLS
  certificates. If using a proxy, prevent access logs from retaining visitor IPs.
- Keep SSH and the database off the public internet.
- Add firewall rules, strong admin credentials, updates, and basic monitoring.
- Update the portfolio tracker from localhost to the final HTTPS script URL.

Exit check: a production portfolio visit appears in analytics; mixed-content and
CORS errors are absent; the database and SSH are not publicly reachable.

## Phase 6 — Automate last

Goal: automate a manual process that is already understood and recoverable.

- Add validation for the Compose configuration.
- Add dependency/image update policy.
- Add CI/CD with narrow credentials and a health check.
- Document rollback; test a failed deployment safely.

## Later project — RAG server

Treat RAG as a separate service and capacity-planning exercise. Do not assume a Pi
2 that handles analytics can also run embeddings, a vector database, and model
inference. Begin by measuring storage, memory, latency, and where embeddings/models
will actually execute.
