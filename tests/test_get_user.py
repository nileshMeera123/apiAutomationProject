from utils.api_client import APIClient

def test_get_single_user():
    client = APIClient()

    response = client.get("/users/2")

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2