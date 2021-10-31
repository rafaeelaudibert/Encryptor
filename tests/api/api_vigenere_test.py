import pytest


def test_vigenere_encrypt_api(client):
    response = client.get("/api/vigenere/encrypt/encryptthis?key=abra").get_json()
    assert response["status"] == 200
    assert response["content"] == "FPUSZRfUIKe"


def test_vigenere_encrypt_api_no_key(client):
    response = client.get("/api/vigenere/encrypt/encryptthis").get_json()
    assert response["status"] == 200
    assert response["content"] == "FPUSZRfUIKe"


def test_vigenere_decrypt_api(client):
    response = client.get("/api/vigenere/decrypt/EGUSZRfUIKe?key=abra").get_json()
    assert response["status"] == 200
    assert response["content"] == "decryptthis"


def test_vigenere_decrypt_api_no_key(client):
    response = client.get("/api/vigenere/decrypt/EGUSZRfUIKe").get_json()
    assert response["status"] == 200
    assert response["content"] == "decryptthis"


def test_vigenere_encrypt_invalid_key(client):
    response = client.get("/api/vigenere/encrypt/encryptthis?key=5").get_json()
    assert response["status"] == 400


def test_vigenere_decrypt_invalid_key(client):
    response = client.get("/api/vigenere/decrypt/EGUSZRfUIKe?key=5").get_json()
    assert response["status"] == 400
