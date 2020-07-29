from werkzeug.exceptions import HTTPException

class InvalidCarException(HTTPException):
    def __init__(self, msg: str = 'Request invalid'):
        super().__init__(msg=msg)