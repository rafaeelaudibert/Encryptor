import pytest
import string
import random

from encryptor.encryptors import Aes
from encryptor.errors import *

def test_encrypt_default():
    text = "hello world"
    ctxt,non = Aes.encrypt(text)
    assert text != ctxt
    plntxt = Aes.decrypt(ctxt, nonce=non)
    assert text == plntxt

def test_encrypt_random_key():
    text = "secret message"
    key = ''.join(random.choice(string.printable) for i in range(16))
    ctxt,non = Aes.encrypt(text, key=key)
    assert text != ctxt
    plntxt = Aes.decrypt(ctxt, key=key, nonce=non)
    assert text == plntxt

def test_decrypt():
	assert Aes.decrypt("ab05593cd5659b6cb379e5", key="*:gw'9yym_pk=j6K", nonce="0f8e828702644bbeabe34a3c303e1a5b") == "don't panic"

