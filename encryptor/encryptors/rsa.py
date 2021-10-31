"""
Encryptor - RSA

https://en.wikipedia.org/wiki/RSA_(cryptosystem)
"""

from binascii import hexlify

from ..errors.not_allowed_value import NotAllowedValue
from ..errors.wrong_type_parameter import WrongTypeParameter
from ..errors.modular_inverse_does_not_exist import ModularInverseDoesNotExist


class Rsa:

    """
	Class implementing RSA cryptosystem
	"""

    DEFAULT_E = 65537
    DEFAULT_P = 296364335885826735335603657657712346243
    DEFAULT_Q = 261610179866133310725739923400935476237
    DEFAULT_N = DEFAULT_P * DEFAULT_Q

    @staticmethod
    def encrypt(text: str, input_n: int = DEFAULT_N, input_e: int = DEFAULT_E):

        """
        RSA - Encrypt

        Call helper functions to encrypt input string
        """

        try:
            input_n = Rsa.DEFAULT_N if input_n is None else int(input_n)
        except ValueError:
            raise WrongTypeParameter("input_n", int, type(input_n))

        try:
            input_e = Rsa.DEFAULT_E if input_e is None else int(input_e)
        except ValueError:
            raise WrongTypeParameter("input_e", int, type(input_e))

        message = int(hexlify(bytes(text, "utf-8")), 16)
        encrypted_message = pow(message, input_e, input_n)
        return hex(encrypted_message)[2:].split("L")[0]

    @staticmethod
    def decrypt(text: str, input_p: int = DEFAULT_P, input_q: int = DEFAULT_Q, input_e: int = DEFAULT_E):

        """
        RSA - Decrypt

        Call helper functions to decrypt input string
        """

        try:
            input_p = Rsa.DEFAULT_P if input_p is None else int(input_p)
        except ValueError:
            raise WrongTypeParameter("input_p", int, type(input_p))

        try:
            input_q = Rsa.DEFAULT_Q if input_q is None else int(input_q)
        except ValueError:
            raise WrongTypeParameter("input_q", int, type(input_q))

        try:
            input_e = Rsa.DEFAULT_E if input_e is None else int(input_e)
        except ValueError:
            raise WrongTypeParameter("input_e", int, type(input_e))

        try:
            encrypted_message = int(text, 16)
        except:
            raise NotAllowedValue

        phi = (input_p - 1) * (input_q - 1)
        delta = Rsa.modinv(input_e, phi)
        num = input_p * input_q
        decrypted_message = pow(encrypted_message, delta, num)
        return hex(decrypted_message)[2:].split("L")[0]

    @staticmethod
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = Rsa.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    @staticmethod
    def modinv(a, m):
        g, x, y = Rsa.egcd(a, m)
        if g != 1:
            raise ModularInverseDoesNotExist(g, a, m)
        else:
            return x % m
