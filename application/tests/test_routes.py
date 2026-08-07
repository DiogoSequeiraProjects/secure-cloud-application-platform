def test_homepage(client):

    response = client.get("/")

    assert response.status_code == 200


def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"

    assert data["application"] == "Secure Cloud Platform"


def test_metrics(client):

    response = client.get("/metrics")

    assert response.status_code == 200

    data = response.get_json()

    assert data["pipeline"] == "GitHub Actions"
