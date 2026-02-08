
def test_create_user(api_client):

    """
    test create user
    :param api_client:
    :return:
    """

    payload = {
        "name": "Nilesh",
        "job": "QA Engineer"
    }

    response = api_client.post("/users", payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Nilesh"