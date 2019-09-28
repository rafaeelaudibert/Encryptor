import pytest


def test_ceasar_encrypt_api(client):
    response = client.get('/api/ceasar/encrypt/encryptthis/2').get_json()
    assert response['status'] == 200
    assert response['content'] == 'gpetarvvjku'


def test_ceasar_encrypt_invalid_api(client):
    response = client.get('/api/ceasar/encrypt/encryptthis00/2').get_json()
    assert response['status'] == 400


def test_ceasar_decrypt_api(client):
    response = client.get('/api/ceasar/decrypt/fgetarvvjku/2').get_json()
    assert response['status'] == 200
    assert response['content'] == 'decryptthis'


def test_ceasar_decrypt_invalid_api(client):
    response = client.get('/api/ceasar/decrypt/fgetarvvjku00/2').get_json()
    assert response['status'] == 400
