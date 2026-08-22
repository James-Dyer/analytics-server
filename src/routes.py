from flask import Blueprint, current_app, jsonify
from sqlalchemy import text

main = Blueprint("main", __name__)


@main.get("/healthz")
def healthz():
    engine = current_app.extensions["database_engine"]

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return jsonify(status="ok", database="ok")
