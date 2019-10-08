import pytest

from encryptor.encryptors import Vigenere
from encryptor.errors import *


def test_encrypt_letter():
    """
    Test basic encrypt letters function
    """
    assert Vigenere.encrypt("a", "q") == "R"
    assert Vigenere.encrypt("j", "d") == "N"
    assert Vigenere.encrypt("x", "r") == "j"
    assert Vigenere.encrypt("t", "N") == "B"
    assert Vigenere.encrypt("R", "v") == "H"


def test_encrypt_letter_no_offset():
    """
    Test basic encrypt letters function omitting `key` parameter
    """
    assert Vigenere.encrypt("r") == "S"


def test_decrypt_letter():
    """
    Test basic decrypt letters function with lower and upper case letters
    """
    assert Vigenere.decrypt("R", "q") == "a"
    assert Vigenere.decrypt("N", "d") == "j"
    assert Vigenere.decrypt("j", "r") == "x"
    assert Vigenere.decrypt("B", "N") == "t"
    assert Vigenere.decrypt("H", "v") == "R"


def test_decrypt_letter_no_offset():
    """
    Test basic decrypt letters function omitting `key` parameter
    """
    assert Vigenere.decrypt("S") == "r"


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
