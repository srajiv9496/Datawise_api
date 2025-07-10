import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_dataset(client):
    payload = {
        "name": "Test Dataset",
        "owner": "rajiv",
        "tags": ["sample"]
    }
    response = client.post("/datasets", json=payload)
    assert response.status_code == 201
    assert "name" in response.json

def test_get_datasets(client):
    response = client.get("/datasets")
    assert response.status_code == 200
    assert isinstance(response.json, list)
