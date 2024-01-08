from werkzeug.exceptions import HTTPException


class UserAlreadyExistsException(HTTPException):
    code = 409


class UserEmailOrPasswordInvalidException(HTTPException):
    code = 400
