import pytest

from encryptor.encryptors import Ceasar
from encryptor.errors import *


def test_encrypt_letter():
    """
    Test basic encrypt letters function with lower and upper case letters
    """
    assert Ceasar.encrypt_letter("a", 1) == "b"
    assert Ceasar.encrypt_letter("j", 5) == "o"
    assert Ceasar.encrypt_letter("x", 2) == "z"
    assert Ceasar.encrypt_letter("J", 5) == "O"
    assert Ceasar.encrypt_letter("X", 2) == "Z"


def test_encrypt_letter_no_offset():
    """
    Test basic encrypt letters function omitting `offset` parameter
    """
    assert Ceasar.encrypt_letter("r") == "r"


def test_decrypt_letter():
    """
    Test basic decrypt letters function with lower and upper case letters
    """
    assert Ceasar.decrypt_letter("b", 1) == "a"
    assert Ceasar.decrypt_letter("o", 5) == "j"
    assert Ceasar.decrypt_letter("z", 2) == "x"
    assert Ceasar.decrypt_letter("O", 5) == "J"
    assert Ceasar.decrypt_letter("Z", 2) == "X"


def test_decrypt_letter_no_offset():
    """
    Test basic decrypt letters function omitting `offset` parameter
    """
    assert Ceasar.decrypt_letter("r") == "r"


def test_encrypt_letter_wrap():
    """
    Test basic encrypt letters function, wrapping around the alphabet
    """
    assert Ceasar.encrypt_letter("z", 1) == "a"
    assert Ceasar.encrypt_letter("Z", 5) == "E"


def test_decrypt_letter_wrap():
    """
    Test basic decrypt letters function, wrapping around the alphabet
    """
    assert Ceasar.decrypt_letter("A", 1) == "Z"
    assert Ceasar.decrypt_letter("e", 5) == "z"


def test_encrypt_letter_non_character():
    """
    Assert there is an error when trying to encrypt a non character
    """
    with pytest.raises(NotAllowedValue):
        assert Ceasar.encrypt_letter("0", 10)


def test_decrypt_letter_non_character():
    """
    Assert there is an error when trying to decrypt a non character
    """
    with pytest.raises(NotAllowedValue):
        assert Ceasar.decrypt_letter("0", 10)


def test_encrypt_letter_wrap_long():
    """
    Test basic encrypt letters function, wrapping around 1 or more times
    """
    assert Ceasar.encrypt_letter("j", 30) == "n"
    assert Ceasar.encrypt_letter("Z", 94) == "P"


def test_decrypt_letter_wrap_long():
    """
    Test basic decrypt letters function, wrapping around 1 or more times
    """
    assert Ceasar.decrypt_letter("N", 30) == "J"
    assert Ceasar.decrypt_letter("p", 94) == "z"


def test_encrypt():
    """
    Test basic encrypt text function, with lower and upper case characters
    """
    assert Ceasar.encrypt("abcdefghijklmn", 1) == "bcdefghijklmno"
    assert Ceasar.encrypt("jklmnop", 5) == "opqrstu"
    assert Ceasar.encrypt("xyza", 2) == "zabc"
    assert Ceasar.encrypt("XYZA", 2) == "ZABC"


def test_encrypt_no_offset():
    """
    Test basic encrypt text function, omitting `offset` parameter
    """
    assert Ceasar.encrypt("abdef") == "abdef"


def test_decrypt():
    """
    Test basic decrypt text function, with lower and upper case characters
    """
    assert Ceasar.decrypt("bcdefghijklmno", 1) == "abcdefghijklmn"
    assert Ceasar.decrypt("opqrstu", 5) == "jklmnop"
    assert Ceasar.decrypt("zabc", 2) == "xyza"
    assert Ceasar.decrypt("ZABC", 2) == "XYZA"


def test_decrypt_no_offset():
    """
    Test basic decrypt text function, omitting `offset` parameter
    """
    assert Ceasar.decrypt("abdef") == "abdef"


def test_encrypt_non_character():
    """
    Assert there is an error when trying to encrypt a text with a non character
    """
    with pytest.raises(NotAllowedValue):
        assert Ceasar.encrypt("abcdefh0", 10)


def test_decrypt_non_character():
    """
    Assert there is an error when trying to decrypt a text with a non character
    """
    with pytest.raises(NotAllowedValue):
        assert Ceasar.decrypt("abcdefh0", 10)


def test_encrypt_wrap_long():
    """
    Test basic encrypt text function, wrapping around 1 or more times
    """
    assert Ceasar.encrypt("jklmnop", 30) == "nopqrst"
    assert Ceasar.encrypt("zanj", 94) == "pqdz"
    assert Ceasar.encrypt("ZANJ", 94) == "PQDZ"


def test_decrypt_wrap_long():
    """
    Test basic decrypt text function, wrapping around 1 or more times
    """
    assert Ceasar.decrypt("npqusn", 30) == "jlmqoj"
    assert Ceasar.decrypt("pasdads", 94) == "zkcnknc"
    assert Ceasar.decrypt("PASDADS", 94) == "ZKCNKNC"


def test_encrypt_caps_alternate():
    """
    Test basic encrypt text function, with upper and lower case characters in the same text
    """
    assert Ceasar.encrypt("AbCdEf", 5) == "FgHiJk"


def test_decrypt_caps_alternate():
    """
    Test basic decrypt text function, with upper and lower case characters in the same text
    """
    assert Ceasar.decrypt("FgHiJk", 5) == "AbCdEf"
