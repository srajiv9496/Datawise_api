def test_create_dataset(client):
    response = client.post("/datasets", json={...})
    assert response.status_code == 201
