def test_get_items_by_purchase_order_id(test_client, get_headers, seed_db):
    response = test_client.get(
        f'/purchase_orders/{seed_db["po"].id}/items', headers=get_headers)

    assert response.status_code == 200
    assert response.json[0]['id'] == seed_db['poi'].id
    assert response.json[0]['description'] == seed_db['poi'].description
    assert response.json[0]['price'] == seed_db['poi'].price
    assert response.json[0]['purchase_order_id'] == seed_db['poi'].purchase_order_id
    assert response.json[0]['quantity'] == seed_db['poi'].quantity


def test_get_items_purchase_id_not_found(test_client, get_headers):
    response = test_client.get(
        '/purchase_orders/99999/items', headers=get_headers)

    assert response.status_code == 404
    assert response.json['error'] == 'Pedido não encontrado.'


def test_post_purchase_order_item(test_client, get_headers, seed_db):
    obj = {
        'description': 'Item teste',
        'price': 16.59,
        'quantity': 5
    }

    response = test_client.post(
        f'/purchase_orders/{seed_db["po"].id}/items', json=obj, content_type='application/json', headers=get_headers)

    assert response.status_code == 201
    assert response.json['id'] is not None
    assert response.json['description'] == obj['description']
    assert response.json['price'] == obj['price']
    assert response.json['quantity'] == obj['quantity']


# def test_post_purchase_order_item_invalid_quantity(test_client, seed_db):
#     obj = {
#         'description': 'Item teste',
#         'price': 16.59,
#         'quantity': 30
#     }

#     response = test_client.post(
#         f'/purchase_orders/{seed_db["po"].id}/items', json=obj, content_type='application/json')

#     assert response.status_code == 400
#     assert response.json['message'] == 'Você somente pode adicionar mais 20 itens'


def test_post_invalid_description(test_client, get_headers, seed_db):
    obj = {
        'price': 20.49,
        'quantity': 30
    }

    response = test_client.post(
        f'/purchase_orders/{seed_db["po"].id}/items', json=obj, content_type='application/json', headers=get_headers)

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descrição'


def test_post_invalid_price(test_client, get_headers, seed_db):
    obj = {
        'description': 'Item teste',
        'quantity': 30
    }

    response = test_client.post(
        f'/purchase_orders/{seed_db["po"].id}/items', json=obj, content_type='application/json', headers=get_headers)

    assert response.status_code == 400
    assert response.json['message']['price'] == 'Informe um preço'


def test_post_invalid_quantity(test_client, get_headers, seed_db):
    obj = {
        'description': 'Item teste',
        'price': 20.22
    }

    response = test_client.post(
        f'/purchase_orders/{seed_db["po"].id}/items', json=obj, content_type='application/json', headers=get_headers)

    assert response.status_code == 400
    assert response.json['message']['quantity'] == 'Informe uma quantidade'


def test_post_items_purchase_id_not_found(test_client, get_headers):
    obj = {
        'description': 'descricao teste',
        'price': 20.55,
        'quantity': 30
    }

    response = test_client.post(
        '/purchase_orders/99999/items', json=obj, content_type='application/json', headers=get_headers)

    assert response.status_code == 404
    assert response.json['error'] == 'Pedido não encontrado.'
