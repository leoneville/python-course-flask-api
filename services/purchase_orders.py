from models import PurchaseOrderModel
from exceptions.purchase_orders import QuantityException


class PurchaseOrdersService:

    def _check_quantity(self, quantity: int):
        if quantity < 50 or quantity > 150:
            raise QuantityException(
                'A quantidade deve ser entre 50 e 150 itens.')

    def find_all(self):
        purchase_orders = PurchaseOrderModel.find_all()
        return [p.as_dict() for p in purchase_orders], 200

    def create(self, **kwargs):
        self._check_quantity(kwargs['quantity'])

        purchase_order = PurchaseOrderModel(**kwargs)
        purchase_order.save()

        return purchase_order.as_dict(), 201

    def find_by_id(self, id: int):
        purchase_order = PurchaseOrderModel.find_by_id(id)

        if purchase_order is None:
            return {"message": "Pedido não encontrado."}, 404

        return purchase_order.as_dict(), 200
