from models import PurchaseOrdersItemsModel, PurchaseOrderModel
from exceptions.purchase_orders_items import QuantityException


class PurchaseOrdersItemsService:

    # def _check_maximum_purchase_order_quantity(self):
    #     raise QuantityException('Você somente pode adicionar mais 20 itens')

    def find_by_purchase_order_id(self, purchase_order_id: int):
        purchase_order = PurchaseOrderModel.find_by_id(purchase_order_id)
        if purchase_order is None:
            return {'error': 'Pedido não encontrado.'}, 404

        purchase_orders_items = PurchaseOrdersItemsModel.find_by_purchase_order_id(
            purchase_order_id)

        return [item.as_dict() for item in purchase_orders_items], 200

    def create(self, **kwargs):
        purchase_order = PurchaseOrderModel.find_by_id(
            kwargs['purchase_order_id'])
        if purchase_order is None:
            return {'error': 'Pedido não encontrado.'}, 404

        purchase_orders_item = PurchaseOrdersItemsModel(
            **kwargs)
        purchase_orders_item.save()

        return purchase_orders_item.as_dict(), 201
