from dataclasses import dataclass

from db import db


@dataclass
class PurchaseOrdersItemsModel(db.Model):
    __tablename__ = 'purchase_orders_items'

    id: int = db.Column(db.Integer, primary_key=True)
    description: str = db.Column(db.Text, nullable=False)
    price: float = db.Column(db.Float(precision=2), nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)
    purchase_order_id: int = db.Column(db.Integer, db.ForeignKey(
        'purchase_order.id'), nullable=False)

    def __init__(self, description: str, price: float, purchase_order_id: int, quantity: int):
        self.description = description
        self.price = price
        self.purchase_order_id = purchase_order_id
        self.quantity = quantity

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int):
        return db.session.get(cls, _id)

    @classmethod
    def find_by_purchase_order_id(cls, _purchase_order_id: int):
        return cls.query.filter_by(purchase_order_id=_purchase_order_id).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
