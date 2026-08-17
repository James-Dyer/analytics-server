# Progress

## Current Phase

The Raspberry Pi 2 is reachable over Ethernet and WiFi with SSH key
authentication. ARMv7 image compatibility has been investigated, and the
repository now targets Offen with SQLite. Ready to install Docker and validate
the service on the Pi.

---

## Status

- `Project-Overview.md` written; reflects current requirements and scope
- `analytics-server` repository created and scaffolded
- ✅ Analytics platform selected: **Offen Fair Web Analytics**
- ✅ Umami rejected for production because its image does not publish ARMv7
- ✅ `offen/offen:v1.4.2` confirmed to publish `linux/arm/v7`
- ✅ `docker-compose.yml` updated for pinned Offen + persistent SQLite
- ✅ `.env`-based Offen secret remains excluded from Git
- ✅ `.env` and `.env.*` patterns added to `.gitignore`
- ✅ Earlier Umami proof of concept ran locally at `http://localhost:3000`
- ⬜ Replace the portfolio's old Umami tracking script with Offen's script
- ✅ Raspberry Pi OS Lite flashed, updated, and first boot completed
- ✅ Pi revision, reported architecture, storage, and network recorded in
  `docs/project-details-2026-08-15.md`
- ✅ Linux user, hostname, and LAN SSH access configured
- ✅ SSH key authentication configured and password SSH login disabled
- ✅ Ralink RT5370 WiFi adapter connected; Ethernet retains the preferred route
- ⬜ Firewall, DHCP reservation, and backups configured and documented
- ⬜ Offen runtime resource use and SQLite persistence validated on the Pi
- ⬜ Linux server set up
- ✅ SSH access configured from dev machine over the local network
- ⬜ GitHub Actions deployment pipeline
- ⬜ Secure HTTPS ingress configured
- ⬜ Update tracking script `src` to point at real server URL

---

## Open Decisions

### Infrastructure
- Whether 1 GB RAM is sufficient for Offen during startup and normal operation
- HTTPS ingress choice (Offen AutoTLS or a privacy-aware reverse proxy)
- Whether to reserve an Ethernet address with DHCP
- Remote access strategy (LAN-only SSH preferred; do not expose SSH directly)
- Authentication

### CI/CD
Exact GitHub Actions pipeline implementation not yet designed.

---

## Hardware Prep

The Pi was flashed and inspected on 2026-08-15. The dated snapshot records a
Raspberry Pi 2 Model B v1.1, 16 GB microSD card, 32-bit Raspberry Pi OS Lite,
working LAN SSH, and Ethernet as the preferred network connection. The
RTL8188CUS WiFi adapter was detected but could not complete authentication due
to an apparent Protected Management Frames policy mismatch. A replacement
Ralink RT5370 adapter now works. Values such as observed LAN addresses and
storage usage are historical and may now be stale.

---

## Next Steps

1. Install Docker and Docker Compose on the Pi
2. Learn basic navigation, permissions, processes, services, packages, and logs
3. Generate the Offen secret and create the first account locally on the Pi
4. Deploy Offen and measure startup/idle CPU, memory, storage, and temperature
5. Verify SQLite persistence across container and device restarts; test backup/restore
6. Add secure HTTPS ingress, then replace the portfolio tracking script
7. Add deployment automation only after the manual workflow is repeatable
