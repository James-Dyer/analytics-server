from analytics.models import Event


def test_dashboard_without_events(client):
    response = client.get("/dashboard/")

    assert response.status_code == 200
    assert b'<p id="total-views">0</p>' in response.data
    assert b'<p id="total-sessions">0</p>' in response.data
    assert b"No events yet" in response.data
    assert b"No page views recorded" in response.data


def test_dashboard_displays_event_summary(client, app):
    session_factory = app.extensions["session_factory"]

    with session_factory.begin() as session:
        session.add_all(
            [
                Event(
                    event_type="pageview",
                    path="/projects",
                    referrer_host="www.google.com",
                    session_id="session-1",
                ),
                Event(
                    event_type="pageview",
                    path="/projects",
                    referrer_host=None,
                    session_id="session-1",
                ),
                Event(
                    event_type="pageview",
                    path="/about",
                    referrer_host=None,
                    session_id="session-2",
                ),
            ]
        )

    response = client.get("/dashboard/")

    assert response.status_code == 200
    assert b'<p id="total-views">3</p>' in response.data
    assert b'<p id="total-sessions">2</p>' in response.data
    assert b"/projects" in response.data
    assert b"/about" in response.data
    assert b"No events yet" not in response.data
