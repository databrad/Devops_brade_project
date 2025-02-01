from app.models import Product
from app.db import db

def test_product_model(app):
    product = Product(name="Test Product", description="Test Description", price=9.99)
    db.session.add(product)
    db.session.commit()

    saved_product = Product.query.first()
    assert saved_product.name == "Test Product"
    assert saved_product.description == "Test Description"
    assert saved_product.price == 9.99
