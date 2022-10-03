import pytest

def test_aes_default_key_full(client):
    response = client.get("/api/aes/encrypt/helloworld").get_json()
    assert response["status"] == 200
    cipher = response["content"]["ciphertext"]
    nonce = response["content"]["nonce"]
    response = client.get(f"/api/aes/decrypt/{cipher}?nonce={nonce}").get_json()
    assert response["status"] == 200
    assert response["content"] == "helloworld"

def test_aes_alternate_key_full(client):
    response = client.get("/api/aes/encrypt/holamundo?key=abcdefghijklmnop").get_json()
    assert response["status"] == 200
    cipher = response["content"]["ciphertext"]
    nonce = response["content"]["nonce"]
    response = client.get(f"/api/aes/decrypt/{cipher}?key=abcdefghijklmnop&nonce={nonce}").get_json()
    assert response["status"] == 200
    assert response["content"] == "holamundo"

