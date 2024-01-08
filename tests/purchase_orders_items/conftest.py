import pytest

from db import db
from models import PurchaseOrdersItemsModel, PurchaseOrderModel


@pytest.fixture()
def seed_db():
    po = PurchaseOrderModel(
        'Purchase Order 1',
        50
    )
    db.session.add(po)
    db.session.commit()

    poi = PurchaseOrdersItemsModel(
        description='Item do pedido 1',
        price=20.55,
        purchase_order_id=po.id,
        quantity=30
    )

    db.session.add(poi)
    db.session.commit()

    yield {'po': po, 'poi': poi}


@pytest.fixture(scope='function', autouse=True)
def clear_db(request):
    if 'nocleardb' in request.keywords:
        return

    db.session.query(PurchaseOrdersItemsModel).delete()
    db.session.query(PurchaseOrderModel).delete()
    db.session.commit()
