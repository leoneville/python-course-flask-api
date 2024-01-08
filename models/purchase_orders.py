from db import db
from dataclasses import dataclass


@dataclass
class PurchaseOrderModel(db.Model):
    __tablename__ = 'purchase_order'

    id: int = db.Column(db.Integer, primary_key=True)
    description: str = db.Column(db.Text, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)

    def __init__(self, description: str, quantity: int):
        self.description = description
        self.quantity = quantity

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def find_all(cls):
        return cls.query.all()  # select * from purchase_order

    @classmethod
    def find_by_id(cls, _id: int):
        # select * from purchase_order where id = ?
        return db.session.get(cls, _id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
