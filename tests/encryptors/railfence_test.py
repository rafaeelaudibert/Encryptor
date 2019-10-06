
import pytest

from encryptor.encryptors import RailFence
from encryptor.errors import *


def test_encrypt():
    """

    """
    assert RailFence.encrypt("WE ARE DISCOVERED. FLEE AT ONCE", 3) == "WECRLTEERDSOEEFEAOCAIVDEN"

