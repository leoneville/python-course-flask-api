from werkzeug.exceptions import HTTPException


class QuantityException(HTTPException):
    code = 400
    description = 'A quantidade deve ser entre 50 e 150 itens.'
