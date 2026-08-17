# First Hands-on Session: Flash and Inspect the Pi

The purpose of this session is not to install analytics software. It is to
create a known, reachable Linux host and learn what hardware is actually
available.

## Before flashing

Collect:

- Raspberry Pi 2 (record the revision printed on the board)
- Stable power supply appropriate for the board
- Reliable microSD card and card reader
- Supported USB WiFi adapter, because Pi 2 has no built-in WiFi
- Optional Ethernet cable for a simpler first connection

## Flash

1. Install and open Raspberry Pi Imager on the development laptop.
2. Choose the exact Pi model and Raspberry Pi OS Lite recommended by Imager.
3. In OS customisation, set a unique hostname, create a non-default user, configure
   WiFi country/SSID/password, set the timezone, and enable SSH.
4. Prefer public-key SSH authentication if Imager offers it and you already
   understand which public key is being installed; otherwise use a strong temporary
   password and convert to keys after the first successful login.
5. Write and verify the card, eject it safely, insert it, and boot the Pi.

Do not paste WiFi passwords, private SSH keys, or application secrets into this repo.

## Connect

Try the hostname selected in Imager from the development laptop:

```bash
ssh YOUR_USER@YOUR_HOSTNAME.local
```

If that fails, use your router's connected-device list to find the Pi's LAN IP.
Do not configure internet port forwarding.

## Inspect before installing anything

Run these one at a time. Read the output and record only non-secret facts in the
session notes below.

```bash
cat /proc/device-tree/model; echo
uname -m
cat /etc/os-release
free -h
lsblk
ip address
ip route
systemctl --failed
```

Questions to answer:

1. What exact Pi revision is this?
2. Does `uname -m` report `armv7l`, `aarch64`, or something else?
3. How much memory and swap are available after boot?
4. Which interface owns the LAN address: Ethernet or WiFi?
5. What is the default route, and why is it needed?
6. Are any services failed?

## Update safely

After inspection, use APT to refresh package information and install upgrades.
Before running commands, explain the difference between updating the package index
and upgrading installed packages. Reboot if required, then prove that SSH reconnects.

## Session notes

- Board model/revision:
- CPU architecture (`uname -m`):
- OS and version:
- RAM / swap:
- Storage device and capacity:
- Network interface and LAN IP:
- Failed services:
- Questions or unexpected output:
