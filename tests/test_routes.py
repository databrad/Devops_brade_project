def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_create_product(client):
    response = client.post('/products', json={
        "name": "New Product",
        "description": "A new product description",
        "price": 19.99
    })
    assert response.status_code == 201
    data = response.json
    assert data['name'] == "New Product"
    assert data['price'] == 19.99

def test_get_products(client):
    # Create a product first
    client.post('/products', json={
        "name": "Another Product",
        "description": "Another product description",
        "price": 29.99
    })

    response = client.get('/products')
    assert response.status_code == 200
    data = response.json
    assert len(data) == 1
    assert data[0]['name'] == "Another Product"

def test_update_product(client):
    # Create a product
    response = client.post('/products', json={
        "name": "Old Product",
        "description": "Old description",
        "price": 9.99
    })
    product_id = response.json['id']

    # Update the product
    response = client.put(f'/products/{product_id}', json={
        "name": "Updated Product",
        "description": "Updated description",
        "price": 14.99
    })
    assert response.status_code == 200
    data = response.json
    assert data['name'] == "Updated Product"
    assert data['price'] == 14.99

def test_delete_product(client):
    # Create a product
    response = client.post('/products', json={
        "name": "Product to Delete",
        "description": "This will be deleted",
        "price": 10.99
    })
    product_id = response.json['id']

    # Delete the product
    response = client.delete(f'/products/{product_id}')
    assert response.status_code == 200
    assert response.json == {"message": "Product deleted successfully"}
