from dataclasses import dataclass
from passlib.hash import pbkdf2_sha256

from db import db


@dataclass
class UserModel(db.Model):
    __tablename__ = 'users'

    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(100), nullable=False, unique=True)
    password: str = db.Column(db.String(300), nullable=False)

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = pbkdf2_sha256.hash(password)

    def as_dict(self):
        return {
            "id": self.id,
            "email": self.email
        }

    @classmethod
    def find_by_email(cls, _email: str):
        return cls.query.filter_by(email=_email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
