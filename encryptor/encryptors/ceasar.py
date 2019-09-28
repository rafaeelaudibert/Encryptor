from ..errors.not_allowed_value import NotAllowedValue


class Ceasar():
    UPPERCASE_OFFSET = 65
    LOWERCASE_OFFSET = 97
    ALPHABET_LENGTH = 26

    @staticmethod
    def encrypt(text: str, offset: int = 0):
        return ''.join([Ceasar.encrypt_letter(char, offset) for char in text])

    @staticmethod
    def decrypt(text: str, offset: int = 0):
        return ''.join([Ceasar.decrypt_letter(char, offset) for char in text])

    @staticmethod
    def encrypt_letter(char, offset):
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
    def decrypt_letter(char, offset):
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
