"""
modular_inverse_does_not_exist

Raises error when modular inverse of 2 parameters does not exist
"""

from werkzeug.exceptions import BadRequest


class ModularInverseDoesNotExist(BadRequest):
    """
	Raised when modular inverse of 2 parameters does not exist probably because there gcd > 1
	"""

    def __init__(self, gcd, p1, p2):
        BadRequest.__init__(
            "Modular inverse does not exist, gcd of {} and {} is {} which is > 1".format(
                p1, p2, gcd
            )
        )
