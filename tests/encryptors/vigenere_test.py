import pytest

from encryptor.encryptors import Vigenere
from encryptor.errors import *


def test_encrypt():
    """
    Test basic encrypt text function, with lower and upper case characters
    """
    assert Vigenere.encrypt("abcdefghijklmn", "abc") == "BDFEGIHJLKMONP"
    assert Vigenere.encrypt("jklmnop", "add") == "KOPNRSQ"
    assert Vigenere.encrypt("xyza", "ahs") == "YamB"
    assert Vigenere.encrypt("XYZA", "sss") == "KLM4"


def test_decrypt():
    """
    Test basic decrypt text function, with lower and upper case characters
    """
    assert Vigenere.decrypt("BDFEGIHJLKMONP", "abc") == "abcdefghijklmn"
    assert Vigenere.decrypt("KOPNRSQ", "add") == "jklmnop"
    assert Vigenere.decrypt("YamB", "ahs") == "xyza"
    assert Vigenere.decrypt("KLM4", "sss") == "XYZA"
