
def test_create_user(api_client):


    payload = {
        "name": "Nilesh",
        "job": "QA Engineer"
    }

    response = api_client.post("/users", payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Nilesh"