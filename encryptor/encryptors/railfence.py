from ..errors.not_allowed_value import NotAllowedValue
from ..errors.wrong_type_parameter import WrongTypeParameter


class RailFence:

    DEFAULT_RAILS = 3
    FILLER_CHARACTER = '.'
    DECRYPTION_POINTER = '#'

    @staticmethod
    def encrypt(text: str, rail_height: int = DEFAULT_RAILS):
        try:
            rail_height = int(rail_height)
        except ValueError:
            raise WrongTypeParameter("rail_height", int, type(rail_height))
        """
        to make railfence work as in most examples we must first clear the
        text of all extra stuff (special characters, etc)
        """

        new_text = []
        for c in text:
            if c.isalnum() or c == ' ':
                new_text.append(c)
        text = ''.join(new_text)

        # edge case handling
        if rail_height == 1:
            return text

        msg_railified = RailFence._get_rail_from_text(text, rail_height)

        out_str = []
        for cy in range(rail_height):
            for cx in range(len(text)):
                if msg_railified[cy][cx] != RailFence.FILLER_CHARACTER:
                    out_str.append(msg_railified[cy][cx])

        return ''.join(out_str)

    @staticmethod
    def decrypt(cipher_text: str, rail_height: int = DEFAULT_RAILS):
        try:
            rail_height = int(rail_height)
        except ValueError:
            raise WrongTypeParameter("rail_height", int, type(rail_height))


        # edge case handling
        if rail_height == 1:
            return cipher_text

        msg_railified = RailFence._get_rail_from_cipher_text(cipher_text, rail_height)

        out_str = []
        for cx in range(len(cipher_text)):
            for cy in range(rail_height):
                if msg_railified[cy][cx] != RailFence.FILLER_CHARACTER:
                    out_str.append(msg_railified[cy][cx])

        return ''.join(out_str)

    @staticmethod
    def _get_rail_from_text(text: str, rail_height: int):
        msg_railified = [[RailFence.FILLER_CHARACTER for _ in range(len(text))]
                          for _ in range(rail_height)]

        x = 0
        y = 0
        going_down = False

        for x in range(len(text)):
            if y == 0 or y == rail_height-1:
                going_down = not going_down

            msg_railified[y][x] = text[x]

            y += 1 if going_down else -1

        return msg_railified


    @staticmethod
    def _get_rail_from_cipher_text(cipher_text: str, rail_height: int):
        msg_railified = [[RailFence.FILLER_CHARACTER for _ in range(len(cipher_text))]
                          for _ in range(rail_height)]
        x = 0
        y = 0

        going_down = False

        for x in range(len(cipher_text)):
            if y == 0 or y == rail_height-1:
                going_down = not going_down

            msg_railified[y][x] = RailFence.DECRYPTION_POINTER

            y += 1 if going_down else -1


        in_cipher = 0
        for cy in range(rail_height):
            for cx in range(len(cipher_text)):
                if msg_railified[cy][cx] == RailFence.DECRYPTION_POINTER:
                    msg_railified[cy][cx] = cipher_text[in_cipher]
                    in_cipher += 1

        return msg_railified





