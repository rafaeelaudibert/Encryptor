from os import urandom
import pytest

# We use this just to get all the available modes
from encryptor.encryptors import Blowfish


def _test_string_in_mode(client, s, mode):
    response = client.get("/api/blowfish/encrypt/%s?mode=%s" % (s, mode)).get_json()
    assert response["status"] == 200
    encrypted = response["content"]

    response = client.get(
        "/api/blowfish/decrypt/%s?mode=%s" % (encrypted, mode)
    ).get_json()
    assert response["status"] == 200

    decrypted = response["content"]

    assert str(s) == decrypted


def test_all_modes_api(client):
    test_string = "some data i want to encode"
    for mode in Blowfish.AVAILABLE_MODES:
        _test_string_in_mode(client, test_string, mode)
