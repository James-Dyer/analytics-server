from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.get("/healthz")
def healthz():
    return jsonify(status="ok")
