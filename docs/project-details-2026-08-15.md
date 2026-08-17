# Home Server Project Details

Snapshot date: 2026-08-15

This document records the Raspberry Pi home-server state observed on the date above. It is a point-in-time snapshot: addresses, package versions, storage usage, network state, and configuration may have changed since it was written.

## Hardware

- Raspberry Pi 2 Model B v1.1
- 16 GB microSD card
- Micro-USB power supply
- Wired Ethernet connection
- Realtek RTL8188CUS (`0bda:8176`) USB 2.4 GHz Wi-Fi adapter
- Keyboard and display available for direct configuration

## Operating system

- Raspberry Pi OS Lite, 32-bit
- Reported operating system: Raspbian GNU/Linux 13 (Trixie)
- Reported kernel: `6.18.39+rpt-rpi-v7`
- Reported architecture: `arm`
- Hostname: `james-home-server`
- Primary user: `jdyer`

The operating system was freshly flashed, booted successfully, and updated after installation.

## Access and networking

- SSH is enabled and works from the local network.
- Normal connection command from the Mac:

  ```bash
  ssh jdyer@james-home-server.local
  ```

- Observed Ethernet IPv4 address: `192.168.12.23`
- The IPv4 address was assigned by the local network and may change unless it is reserved in the router.
- The server is currently intended for local-network access only.
- No internet-facing SSH port forwarding has been configured.

## Storage snapshot

At the time of inspection, the root filesystem reported:

- Total: approximately 15 GB
- Used: approximately 2.9 GB
- Available: approximately 11 GB
- Utilization: 21%

The boot partition reported approximately 505 MB total with 425 MB available.

## Wi-Fi status

Wi-Fi setup was intentionally deferred in favor of Ethernet.

Verified observations:

- The RTL8188CUS adapter is detected by USB.
- NetworkManager exposes it as `wlan0`.
- The adapter is not blocked by `rfkill`.
- It can scan and see the `MDNet` network on 2.4 GHz with strong signal.
- `MDNet` advertises WPA2 and WPA3.
- Authentication attempts associated with an access point but did not complete.
- `wpa_supplicant` later reported association rejection status code 31, indicating a Protected Management Frames policy mismatch.

Likely future options are using Ethernet permanently, configuring a separate 2.4 GHz WPA2-only network, or replacing the older Wi-Fi adapter. No further Wi-Fi work is currently planned.

## Security and administration status

- SSH password authentication was used during initial setup.
- SSH-key authentication has not yet been documented as configured.
- A firewall has not yet been documented as configured.
- A DHCP reservation for the Ethernet address has not yet been documented as configured.
- A backup strategy has not yet been established.
- No remote-access VPN has been configured.
- No application services had been installed on the Pi. The source notes also
  described services for the host as not yet selected; this repository already
  had a local Umami proof of concept, so treat that wording as scoped to the Pi
  deployment rather than the project-wide platform decision.

Passwords, Wi-Fi credentials, SSH secrets, and other sensitive values are intentionally excluded from this document.
