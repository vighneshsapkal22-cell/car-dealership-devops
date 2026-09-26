from app import app


def test_homepage():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_get_cars():
    client = app.test_client()
    response = client.get("/api/cars")
    assert response.status_code == 200

    data = response.get_json()
    assert len(data) == 5


def test_get_single_car():
    client = app.test_client()
    response = client.get("/api/cars/1")
    assert response.status_code == 200

    data = response.get_json()
    assert data["brand"] == "Toyota"
    assert data["model"] == "Fortuner"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "healthy"