from flask import Blueprint, current_app, jsonify, request
from sqlalchemy import text
from .models import Event

main = Blueprint("main", __name__)


@main.get("/healthz")
def healthz():
    engine = current_app.extensions["database_engine"]

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return jsonify(status="ok", database="ok")


@main.post("/events")
def create_event():
    payload = request.get_json(silent=True)

    # check if payload is valid JSON
    if not isinstance(payload, dict):
        return jsonify(error="Request body must be JSON"), 400

    event_type = payload.get("event_type")
    path = payload.get("path")
    referrer_host = payload.get("referrer_host")
    session_id = payload.get("session_id")

    if event_type != "pageview":
        return jsonify(error="Unsupported event type"), 400

    if not isinstance(path, str) or not path or len(path) > 512:
        return jsonify(error="Invalid path"), 400

    if referrer_host is not None and (
        not isinstance(referrer_host, str) or len(referrer_host) > 255
    ):
        return jsonify(error="Invalid referrer host"), 400

    if not isinstance(session_id, str) or not session_id or len(session_id) > 64:
        return jsonify(error="Invalid session ID"), 400

    event = Event(
        event_type=event_type,
        path=path,
        referrer_host=referrer_host,
        session_id=session_id,
    )

    session_factory = current_app.extensions["session_factory"]

    with session_factory.begin() as session:
        session.add(event)

    return "", 204
