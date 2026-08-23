import pytest

from sqlalchemy import func, select

from analytics.models import Event


@pytest.mark.parametrize(
    ("payload", "expected_error"),
    [
        (
            {
                "event_type": "click",
                "path": "/projects",
                "session_id": "session-1",
            },
            "Unsupported event type",
        ),
        (
            {
                "event_type": "pageview",
                "session_id": "session-1",
            },
            "Invalid path",
        ),
        (
            {
                "event_type": "pageview",
                "path": "",
                "session_id": "session-1",
            },
            "Invalid path",
        ),
        (
            {
                "event_type": "pageview",
                "path": "/projects",
                "referrer_host": 123,
                "session_id": "session-1",
            },
            "Invalid referrer host",
        ),
        (
            {
                "event_type": "pageview",
                "path": "/projects",
            },
            "Invalid session ID",
        ),
    ],
)
def test_create_event_rejects_invalid_payloads(
    client,
    app,
    payload,
    expected_error,
):
    response = client.post("/events", json=payload)

    assert response.status_code == 400
    assert response.get_json() == {"error": expected_error}

    session_factory = app.extensions["session_factory"]

    with session_factory() as session:
        event_count = session.scalar(select(func.count()).select_from(Event))

    assert event_count == 0


def test_create_event(client, app):
    payload = {
        "event_type": "pageview",
        "path": "/projects",
        "referrer_host": "www.google.com",
        "session_id": "test-session-1",
    }

    response = client.post("/events", json=payload)

    assert response.status_code == 204
    assert response.data == b""

    session_factory = app.extensions["session_factory"]

    with session_factory() as session:
        event = session.scalar(select(Event))

        assert event is not None
        assert event.event_type == "pageview"
        assert event.path == "/projects"
        assert event.referrer_host == "www.google.com"
        assert event.session_id == "test-session-1"
        assert event.received_at is not None


def test_create_event_rejects_non_json_body(client):
    response = client.post(
        "/events",
        data="this is not JSON",
        content_type="text/plain",
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Request body must be JSON",
    }
