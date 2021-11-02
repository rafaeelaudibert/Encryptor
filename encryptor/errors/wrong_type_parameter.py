"""
wrong_type_parameter

Raises error when there is invalid value in input
"""

from werkzeug.exceptions import BadRequest


class WrongTypeParameter(BadRequest):
    """ Raised when there is an invalid value in the input """

    def __init__(self, parameter, should_type, received_type):
        super().__init__(
            "The {} parameter received an invalid type. Should be {} and received {}".format(
                parameter, should_type, received_type
            )
        )
