import pytest

from encryptor.encryptors import RailFence
from encryptor.errors import *


def test_encrypt():
    """

    """
    assert (
        RailFence.encrypt("WE ARE DISCOVERED FLEE AT ONCE", 3)
        == "WRIVDETCEAEDSOEE LEA NE  CRF O"
    )
    assert RailFence.encrypt("I REALLY LIKE PUZZLES", 3) == "IA EZS ELYLK UZERLIPL"
    assert RailFence.encrypt("RAILFENCEENCRYPTOR", 2) == "RIFNENRPOALECECYTR"
    assert RailFence.encrypt("RAIL", 5) == "RAIL"
    assert RailFence.encrypt("R", 5) == "R"
    assert RailFence.encrypt("R", 1) == "R"
    assert RailFence.encrypt("R", 100) == "R"


def test_decrypt():
    assert (
        RailFence.decrypt("WRIVDETCEAEDSOEE LEA NE  CRF O", 3)
        == "WE ARE DISCOVERED FLEE AT ONCE"
    )
    assert RailFence.decrypt("IA EZS ELYLK UZERLIPL", 3) == "I REALLY LIKE PUZZLES"
    assert RailFence.decrypt("IAM", 3) == "IAM"
    assert RailFence.decrypt("IAM", 100) == "IAM"
    assert RailFence.decrypt("I", 1) == "I"
    assert RailFence.decrypt("IM", 1) == "IM"


def test_encrypt_without_rail_height():
    assert RailFence.encrypt("Railfence") == "Rfealecin"


def test_decrypt_without_rail_height():
    assert RailFence.decrypt("Rfealecin") == "Railfence"
