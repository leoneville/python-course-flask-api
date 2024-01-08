from resources.users import UserCreation, UserLogin
from resources.purchase_orders_items import PurchaseOrderItems
from resources.purchase_orders import PurchaseOrders, PurchaseOrdersById


def initialize_routes(api):
    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrdersById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrderItems, '/purchase_orders/<int:id>/items')
    api.add_resource(UserCreation, '/users')
    api.add_resource(UserLogin, '/login')
