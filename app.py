from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from db import db
from config import DevelopmentConfig
from resources import initialize_routes


jwt = JWTManager()


def create_app(config_class: str | object):
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config_class)

    db.init_app(app)

    Migrate(app, db)

    jwt.init_app(app)

    @jwt.invalid_token_loader
    def invalid_jwt(error):
        return {"message": "Token de acesso inválido."}, 401

    @jwt.unauthorized_loader
    def unauthorized_jwt(error):
        return {"message": "Sem autorização, por favor informe um token válido."}, 401

    @jwt.expired_token_loader
    def expired_jwt(error, payload):
        return {"message": "Token expirado."}, 401

    initialize_routes(api)

    return app
