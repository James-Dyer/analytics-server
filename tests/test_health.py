def test_healthz_returns_database_status(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == {
        "database": "ok",
        "status": "ok",
    }
