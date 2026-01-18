from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_predict_class_a():
    # Input 0.0 should predict Class A (0)
    response = client.post("/predict", json={"feature": 0.0})
    assert response.status_code == 200
    assert response.json()["prediction"] == 0

def test_predict_class_b():
    # Input 5.0 should predict Class B (1)
    response = client.post("/predict", json={"feature": 5.0})
    assert response.status_code == 200
    assert response.json()["prediction"] == 1

def test_invalid_input():
    # Sending string instead of float should fail validation
    response = client.post("/predict", json={"feature": "invalid"})
    assert response.status_code == 422
