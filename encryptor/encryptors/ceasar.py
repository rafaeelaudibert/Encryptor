from ..errors.not_allowed_value import NotAllowedValue
from ..errors.wrong_type_parameter import WrongTypeParameter


class Ceasar:
    DEFAULT_OFFSET = 0
    UPPERCASE_OFFSET = 65
    LOWERCASE_OFFSET = 97
    ALPHABET_LENGTH = 26

    @staticmethod
    def encrypt(text: str, offset: int = DEFAULT_OFFSET):
        try:
            offset = int(offset)
        except ValueError:
            raise WrongTypeParameter("offset", int, type(offset))

        return "".join([Ceasar.encrypt_letter(char, offset) for char in text])

    @staticmethod
    def decrypt(text: str, offset: int = DEFAULT_OFFSET):
        try:
            offset = int(offset)
        except ValueError:
            raise WrongTypeParameter("offset", int, type(offset))

        return "".join([Ceasar.decrypt_letter(char, offset) for char in text])

    @staticmethod
    def encrypt_letter(char: str, offset: int = DEFAULT_OFFSET):
        # Encrypt uppercase characters in plain text
        if char.isupper():
            return chr((ord(char) + offset - Ceasar.UPPERCASE_OFFSET) %
                       Ceasar.ALPHABET_LENGTH + Ceasar.UPPERCASE_OFFSET)
        # Encrypt lowercase characters in plain text
        elif char.islower():
            return chr((ord(char) + offset - Ceasar.LOWERCASE_OFFSET) %
                       Ceasar.ALPHABET_LENGTH + Ceasar.LOWERCASE_OFFSET)
        else:
            raise NotAllowedValue

    @staticmethod
    def decrypt_letter(char: str, offset: int = DEFAULT_OFFSET):
        # Decrypt uppercase characters in plain text
        if char.isupper():
            return chr((ord(char) - offset - Ceasar.UPPERCASE_OFFSET) %
                       Ceasar.ALPHABET_LENGTH + Ceasar.UPPERCASE_OFFSET)
        # Decrypt lowercase characters in plain text
        elif char.islower():
            return chr((ord(char) - offset - Ceasar.LOWERCASE_OFFSET) %
                       Ceasar.ALPHABET_LENGTH + Ceasar.LOWERCASE_OFFSET)
        else:
            raise NotAllowedValue
