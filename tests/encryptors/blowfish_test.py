import pytest

from encryptor.encryptors import Blowfish
from encryptor.errors import *


def __test_string_in_mode(s, mode):
    encrypted = Blowfish.encrypt(s, mode = mode)
    decrypted = Blowfish.decrypt(encrypted, mode = mode)

    assert s == decrypted


def test_all_modes():
    test_string = 'some_data_i_want_to_encode'
    for mode in Blowfish.AVAILABLE_MODES: 
        __test_string_in_mode(test_string, mode)
