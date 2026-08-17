# Progress

## Current Phase

Local Umami proof of concept complete. The Raspberry Pi 2 has been prepared and
inspected over Ethernet. Ready to validate the analytics stack on the Pi before
selecting the production deployment architecture.

---

## Status

- `Project-Overview.md` written; reflects current requirements and scope
- `analytics-server` repository created and scaffolded
- ✅ Analytics platform selected: **Umami**
- ✅ `docker-compose.yml` written with `.env`-based secrets
- ✅ `.env` and `.env.*` patterns added to `.gitignore`
- ✅ Umami running locally at `http://localhost:3000`
- ✅ Tracking script embedded in portfolio site (pointing at localhost for now)
- ✅ Raspberry Pi OS Lite flashed, updated, and first boot completed
- ✅ Pi revision, reported architecture, storage, and network recorded in
  `docs/project-details-2026-08-15.md`
- ✅ Linux user, hostname, and LAN SSH access configured
- ⬜ SSH keys, firewall, DHCP reservation, and backups configured and documented
- ⬜ Umami and PostgreSQL image compatibility validated on the Pi
- ⬜ Linux server set up
- ✅ SSH access configured from dev machine over the local network
- ⬜ GitHub Actions deployment pipeline
- ⬜ Reverse proxy configured
- ⬜ Update tracking script `src` to point at real server URL

---

## Open Decisions

### Infrastructure
- Whether current Umami and PostgreSQL container images support that architecture
- Whether 1 GB RAM is sufficient for the existing stack
- Reverse proxy choice (nginx, Caddy, Traefik)
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
to an apparent Protected Management Frames policy mismatch. Values such as the
observed LAN address and storage usage are historical and may now be stale.

---

## Next Steps

1. Configure and document SSH keys, firewall policy, DHCP reservation, and backups
2. Learn basic navigation, permissions, processes, services, packages, and logs
3. Test the current containers on the Pi; do not assume ARM compatibility
4. Choose the production stack from the measured results
5. Deploy manually, verify persistence, then add HTTPS and automation
6. Update the portfolio tracking URL only after a stable HTTPS endpoint exists
