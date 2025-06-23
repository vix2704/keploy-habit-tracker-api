<<<<<<< HEAD
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_all_habits():
    response = client.get("/habits/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
=======
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_all_habits():
    response = client.get("/habits/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
>>>>>>> 240859e (Add test suite and update README with coverage)
