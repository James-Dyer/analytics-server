from sqlalchemy.exc import SQLAlchemyError


def test_healthz_returns_database_status(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == {
        "database": "ok",
        "status": "ok",
    }


def test_healthz_returns_503_when_database_is_unavailable(client, app, monkeypatch):
    class UnavailableEngine:
        def connect(self):
            raise SQLAlchemyError("database unavailable")

    monkeypatch.setitem(app.extensions, "database_engine", UnavailableEngine())

    response = client.get("/healthz")

    assert response.status_code == 503
    assert response.get_json() == {
        "database": "error",
        "status": "unhealthy",
    }
