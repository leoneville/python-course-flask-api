import pytest
from exceptions.purchase_orders_items import QuantityException
from services.purchase_orders_items import PurchaseOrdersItemsService


# @pytest.mark.nocleardb
# def test_check_maximum_po_quantity():
#     with pytest.raises(QuantityException) as ex:
#         PurchaseOrdersItemsService()._check_maximum_purchase_order_quantity()

#     assert ex.value.code == 400
#     assert ex.value.description == 'Você somente pode adicionar mais 20 itens'
