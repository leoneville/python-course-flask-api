from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

from models import UserModel
from exceptions.users import UserAlreadyExistsException, UserEmailOrPasswordInvalidException


class UsersService:
    def create(self, **kwargs):
        user = UserModel.find_by_email(kwargs['email'])
        if user:
            raise UserAlreadyExistsException(
                f'Já existe um usuário cadastrado com o email {user.email}')

        new_user = UserModel(**kwargs)
        new_user.save()

        return new_user.as_dict(), 201

    def login(self, **kwargs):
        user = UserModel.find_by_email(kwargs['email'])
        if user and pbkdf2_sha256.verify(kwargs['password'], user.password):
            token = create_access_token(identity=user.id)
            return {'access_token': token}, 200

        raise UserEmailOrPasswordInvalidException(
            'Email ou senha incorretos.')
