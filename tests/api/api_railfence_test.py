import pytest


def test_railfence_encrypt_api(client):
    response = client.get(
        "/api/railfence/encrypt/helloworld?rail_height=2").get_json()
    assert response["status"] == 200
    assert response["content"] == "hloolelwrd"


def test_railfence_encrypt_api_no_offset(client):
    response = client.get("/api/railfence/encrypt/helloworld").get_json()
    assert response["status"] == 200
    assert response["content"] == "holelwrdlo"


def test_railfence_decrypt_api(client):
    response = client.get(
        "/api/railfence/decrypt/hloolelwrd?rail_height=2").get_json()
    assert response["status"] == 200
    assert response["content"] == "helloworld"


def test_ceasar_decrypt_api_no_offset(client):
    response = client.get("/api/railfence/decrypt/holelwrdlo").get_json()
    assert response["status"] == 200
    assert response["content"] == "helloworld"
