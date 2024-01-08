from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from services.purchase_orders_items import PurchaseOrdersItemsService


class PurchaseOrderItems(Resource):
    __service__ = PurchaseOrdersItemsService()
    parser = reqparse.RequestParser()
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Informe uma descrição'
    )
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='Informe um preço'
    )

    parser.add_argument(
        'quantity',
        type=int,
        required=True,
        help='Informe uma quantidade'
    )

    @jwt_required()
    def get(self, id: int):
        return self.__service__.find_by_purchase_order_id(id)

    @jwt_required()
    def post(self, id: int):
        data = PurchaseOrderItems.parser.parse_args()
        data['purchase_order_id'] = id

        return self.__service__.create(**data)
