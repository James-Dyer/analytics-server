from pathlib import Path
from flask import Flask
from .database import init_database


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    app.config.from_mapping(
        DATABASE_URL=(f"sqlite:///{Path(app.instance_path) / 'analytics.db'}")
    )
    if test_config is not None:
        app.config.update(test_config)

    init_database(app)

    from .routes import main
    from .dashboard import dashboard

    app.register_blueprint(dashboard)
    app.register_blueprint(main)

    return app
