def test_health(client):
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.content.decode("utf-8") == "I am alive!"
