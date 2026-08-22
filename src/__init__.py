from pathlib import Path

from flask import Flask

from .database import init_database


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    init_database(app)

    from .routes import main

    app.register_blueprint(main)

    return app
