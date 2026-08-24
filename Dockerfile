FROM python:3.13.15-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd --system analytics \
    && useradd --system --gid analytics --home-dir /app --no-create-home analytics

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir --requirement requirements.txt

COPY analytics ./analytics

RUN mkdir -p /data \
    && chown analytics:analytics /data

USER analytics

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=3)"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--threads", "2", "--timeout", "30", "--no-control-socket", "--access-logfile", "-", "--error-logfile", "-", "analytics:create_app()"]
