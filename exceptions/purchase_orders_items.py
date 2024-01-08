from werkzeug.exceptions import HTTPException


class QuantityException(HTTPException):
    code = 400
    description = 'Você somente pode adicionar mais 20 itens'
