import pytest

def test_transposition_encrypt_api(client):
    response = client.get("/api/transposition/encrypt?key=3&text=test text").get_json()
    assert response["status"] == 200
    assert response["content"] == "ttee xstt"

def test_transposition_decrypt_api(client):
    response = client.get("/api/transposition/decrypt?key=3&text=ttee xstt").get_json()
    assert response["status"] == 200
    assert response["content"] == "test text"