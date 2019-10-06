import pytest


def test_ceasar_encrypt_api(client):
    response = client.get(
        '/api/ceasar/encrypt/encryptthis?offset=2').get_json()
    assert response['status'] == 200
    assert response['content'] == 'gpetarvvjku'


def test_ceasar_encrypt_api_no_offset(client):
    response = client.get(
        '/api/ceasar/encrypt/encryptthis').get_json()
    assert response['status'] == 200
    assert response['content'] == 'encryptthis'


def test_ceasar_encrypt_invalid_api(client):
    response = client.get(
        '/api/ceasar/encrypt/encryptthis00?offset=2').get_json()
    assert response['status'] == 400


def test_ceasar_decrypt_api(client):
    response = client.get(
        '/api/ceasar/decrypt/fgetarvvjku?offset=2').get_json()
    assert response['status'] == 200
    assert response['content'] == 'decryptthis'


def test_ceasar_decrypt_api_no_offset(client):
    response = client.get(
        '/api/ceasar/decrypt/encryptthis').get_json()
    assert response['status'] == 200
    assert response['content'] == 'encryptthis'


def test_ceasar_decrypt_invalid_api(client):
    response = client.get(
        '/api/ceasar/decrypt/fgetarvvjku00?offset=2').get_json()
    assert response['status'] == 400


def test_ceasar_encrypt_invalid_offset(client):
    response = client.get(
        '/api/ceasar/encrypt/fgetarvvjku00?offset=abc').get_json()
    assert response['status'] == 400
    assert 'Should be <class \'int\'>' in response['content']


def test_ceasar_decrypt_invalid_offset(client):
    response = client.get(
        '/api/ceasar/decrypt/fgetarvvjku00?offset=abc').get_json()
    assert response['status'] == 400
    assert 'Should be <class \'int\'>' in response['content']
