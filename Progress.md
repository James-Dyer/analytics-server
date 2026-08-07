# Progress

## Current Phase

Local Umami proof of concept complete. Ready to prepare and inspect the
Raspberry Pi 2 before selecting the production deployment architecture.

---

## Status

- `Project-Overview.md` written; reflects current requirements and scope
- `analytics-server` repository created and scaffolded
- ✅ Analytics platform selected: **Umami**
- ✅ `docker-compose.yml` written with `.env`-based secrets
- ✅ `.env` and `.env.*` patterns added to `.gitignore`
- ✅ Umami running locally at `http://localhost:3000`
- ✅ Tracking script embedded in portfolio site (pointing at localhost for now)
- ⬜ Raspberry Pi OS Lite flashed and first boot completed
- ⬜ Exact Pi revision, CPU architecture, memory, storage, and network recorded
- ⬜ Linux user, updates, hostname, timezone, and SSH configured
- ⬜ Umami and PostgreSQL image compatibility validated on the Pi
- ⬜ Linux server set up
- ⬜ SSH access configured from dev machine
- ⬜ GitHub Actions deployment pipeline
- ⬜ Reverse proxy configured
- ⬜ Update tracking script `src` to point at real server URL

---

## Open Decisions

### Infrastructure
- Exact Raspberry Pi 2 revision and whether the installed OS is 32-bit or 64-bit
- Whether current Umami and PostgreSQL container images support that architecture
- Whether 1 GB RAM is sufficient for the existing stack
- Reverse proxy choice (nginx, Caddy, Traefik)
- Networking approach and static IP
- Remote access strategy (LAN-only SSH preferred; do not expose SSH directly)
- Authentication

### CI/CD
Exact GitHub Actions pipeline implementation not yet designed.

---

## Hardware Prep (Not Started)

Before deploying the analytics stack:
- Confirm the Pi model/revision printed on the board
- Confirm the power supply is appropriate and stable
- Use a reliable microSD card (16 GB or larger is a practical starting point)
- Confirm the WiFi adapter is supported (Pi 2 has no built-in WiFi)
- Flash Raspberry Pi OS Lite using Raspberry Pi Imager
- Preconfigure hostname, user, WiFi, and SSH in Imager
- Record the output of `cat /proc/device-tree/model`, `uname -m`, `free -h`,
  `lsblk`, and `ip address`

---

## Next Steps

1. Inventory the Pi, power supply, microSD card, and WiFi adapter
2. Flash Raspberry Pi OS Lite and complete the first headless boot
3. Connect over SSH and record the hardware/OS facts listed above
4. Learn basic navigation, permissions, processes, services, packages, and logs
5. Test the current containers on the Pi; do not assume ARM compatibility
6. Choose the production stack from the measured results
7. Deploy manually, verify persistence, then add HTTPS and automation
8. Update the portfolio tracking URL only after a stable HTTPS endpoint exists
