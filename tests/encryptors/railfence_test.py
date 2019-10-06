
import pytest

from encryptor.encryptors import RailFence
from encryptor.errors import *


def test_encrypt():
    """

    """
    assert RailFence.encrypt("WE ARE DISCOVERED. FLEE AT ONCE", 3) == "WECRLTEERDSOEEFEAOCAIVDEN"
    assert RailFence.encrypt("I REALLY LIKE PUZZLES", 3) == "ILIUERALLKPZLSEYEZ"
    assert RailFence.encrypt("RAILFENCEENCRYPTOR", 2) == "RIFNENRPOALECECYTR"
    assert RailFence.encrypt("RAIL", 5) == "RAIL"
    assert RailFence.encrypt("R", 5) == "R"
    assert RailFence.encrypt("R", 1) == "R"
    assert RailFence.encrypt("R", 100) == "R"

