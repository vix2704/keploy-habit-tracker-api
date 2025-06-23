from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_all_habits():
    response = client.get("/habits/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
