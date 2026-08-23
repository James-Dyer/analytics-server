import pytest

from analytics import create_app


@pytest.fixture
def app(tmp_path):
    database_path = tmp_path / "test.db"

    app = create_app(
        {
            "TESTING": True,
            "DATABASE_URL": f"sqlite:///{database_path}",
        }
    )

    yield app

    app.extensions["database_engine"].dispose()


@pytest.fixture
def client(app):
    return app.test_client()
