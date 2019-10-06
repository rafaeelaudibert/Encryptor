from ..errors.not_allowed_value import NotAllowedValue
from itertools import cycle


class Vigenere:
    # square or Vigenère table, also known as the tabula recta, can be used for encryption and decryption.
    # may be changed for more secure
    # use ASCII by default
    ALPHABET = {i: chr(i) for i in range(128)}
    KEY = 'abra'

    @staticmethod
    def encrypt(text: str, key: str = KEY, tabula_recta=None):
        if tabula_recta is None:
            tabula_recta = Vigenere.ALPHABET
        if key.isalpha():
            message_encoded = Vigenere._encode(text)
            key_encoded = Vigenere._encode(key)
            compare = Vigenere._comparator(message_encoded, key_encoded)
            encrypt_message = [(value[0] + value[1]) % len(Vigenere.ALPHABET) for value in compare.values()]
            return ''.join(Vigenere._decode(encrypt_message))
        else:
            raise NotAllowedValue

    @staticmethod
    def decrypt(text: str, key: str = KEY, tabula_recta=None):
        if tabula_recta is None:
            tabula_recta = Vigenere.ALPHABET
        if key.isalpha():
            message_decoded = Vigenere._encode(text)
            key_decoded = Vigenere._encode(key)
            compare = Vigenere._comparator(message_decoded, key_decoded)
            decrypt_message = [(value[0] - value[1]) % len(Vigenere.ALPHABET) for value in compare.values()]
            return ''.join(Vigenere._decode(decrypt_message))
        else:
            raise NotAllowedValue

    @staticmethod
    def _encode(word: str):
        return [key for char in word for key, value in Vigenere.ALPHABET.items() if char == value]

    @staticmethod
    def _decode(sequence: list):
        return [value for i in sequence for key, value in Vigenere.ALPHABET.items() if i == key]

    @staticmethod
    def _comparator(message: list, key: list):
        return dict([(i, [char[0], char[1]]) for i, char in enumerate(zip(message, cycle(key)))])
