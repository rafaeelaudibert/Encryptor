from werkzeug.exceptions import BadRequest


class NotAllowedValue(BadRequest):
    ''' Raised when there is an invalid value in the input '''

    def __init__(self, message='A not allowed value was encountered in the input text'):
        super().__init__(message)
