import pytest
from encryptor.encryptors import Transposition

def test_encrypt():
    assert Transposition.encrypt(3, "TEST MESSAGE") == "TTEAE SGSMSE"

def test_decrypt():
    assert Transposition.decrypt(3, "TTEAE SGSMSE") == "TEST MESSAGE"