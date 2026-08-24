import logging
import os
import sys
from pathlib import Path

from flask import Flask
from werkzeug.exceptions import RequestEntityTooLarge

from .database import init_database


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        DATABASE_URL=os.environ.get(
            "DATABASE_URL",
            f"sqlite:///{Path(app.instance_path) / 'analytics.db'}",
        ),
        LOG_LEVEL=os.environ.get("LOG_LEVEL", "INFO"),
        MAX_CONTENT_LENGTH=int(os.environ.get("MAX_CONTENT_LENGTH", "8192")),
    )
    if test_config is not None:
        app.config.update(test_config)

    configure_logging(app)
    init_database(app)

    from .routes import main
    from .dashboard import dashboard

    app.register_blueprint(dashboard)
    app.register_blueprint(main)

    @app.errorhandler(RequestEntityTooLarge)
    def request_too_large(error):
        return {"error": "Request body is too large"}, 413

    return app


def configure_logging(app: Flask) -> None:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s level=%(levelname)s logger=%(name)s message=%(message)s"
        )
    )

    app.logger.handlers.clear()
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config["LOG_LEVEL"].upper())
    app.logger.propagate = False
