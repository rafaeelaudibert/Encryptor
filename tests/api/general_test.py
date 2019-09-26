import pytest


def test_root_api(client):
    response = client.get('/api/').get_json()
    assert 'content' in response.keys()
    assert response['content'] == 'Hello World!'
