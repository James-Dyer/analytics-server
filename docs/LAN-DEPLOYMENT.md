# Raspberry Pi LAN Deployment

This runbook deploys the analytics service on the home LAN only. Do not create
router port-forwarding rules during this phase.

## 1. Inspect the host

Connect to the Pi and confirm the expected architecture and free resources:

```bash
uname -m
free -h
df -h
docker --version
docker compose version
```

`uname -m` should report `armv7l`. This Pi runs 32-bit Raspberry Pi OS 13
(Trixie). Docker's upstream repository no longer publishes current armhf
packages for this combination, so install the compatible packages maintained by
the Raspbian Trixie repository:

```bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
sudo docker version
sudo docker compose version
```

Docker access remains behind `sudo`; the deployment does not add the login user
to Docker's root-equivalent group.

## 2. Deploy manually

Clone the repository on the first deployment, or pull `main` for an existing
clone. From the repository directory:

```bash
sudo docker compose build
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail=100 analytics
```

Wait for the service to report `healthy`. On the Pi:

```bash
curl --fail http://127.0.0.1:3000/healthz
```

From the development laptop, replace the hostname if needed:

```bash
curl --fail http://james-home-server.local:3000/healthz
```

The dashboard should be available on the LAN at
`http://james-home-server.local:3000/dashboard/`.

## 3. Verify collection and persistence

Create a recognizable event from the laptop:

```bash
curl --request POST http://james-home-server.local:3000/events \
  --header 'Content-Type: application/json' \
  --data '{"event_type":"pageview","path":"/pi-persistence-test","referrer_host":null,"session_id":"pi-manual-test"}'
```

Confirm `/pi-persistence-test` appears on the dashboard, then restart only the
container:

```bash
sudo docker compose restart analytics
sudo docker compose ps
```

Reload the dashboard and confirm the event remains. Reboot the Pi, reconnect,
and repeat the health and dashboard checks to prove persistence across a device
restart.

`sudo docker compose down` preserves the named volume. Do not use
`sudo docker compose down --volumes`, which deletes the analytics database.

## 4. Record resource use

After startup and again after several minutes of idle time, record:

```bash
sudo docker stats --no-stream analytics-server-analytics-1
sudo docker top analytics-server-analytics-1 -eo pid,ppid,rss,pcpu,comm
free -h
df -h
sudo docker system df
vcgencmd measure_temp
```

If the generated container name differs, copy it from `docker compose ps`.
Record startup time, container memory and CPU, free storage, and temperature in
`Progress.md`. The Pi 2 kernel does not expose container memory-limit or memory
accounting capabilities, so use process RSS from `docker top` plus host-level
`free` output instead.

## 5. Stop or update

Stop the service without deleting data:

```bash
sudo docker compose down
```

For a manual update:

```bash
git pull --ff-only
sudo docker compose up --build -d
curl --fail http://127.0.0.1:3000/healthz
```

Public HTTPS ingress, dashboard access control, CORS, rate limiting, the browser
tracker, and automated deployment are deliberately deferred until this LAN
deployment is measured and repeatable.
