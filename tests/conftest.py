import pytest
from app import create_app
from app.config import TestConfig
from app.db import db
from app.models import Product

@pytest.fixture
def app():
    app = create_app(TestConfig)
    # app.config.from_object('app.config.TestConfig')

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def sample_data(app):
    """
    Add sample data to the test database.
    """
    with app.app_context():
        product1 = Product(name="Sample Product 1", description="First sample", price=10.99)
        product2 = Product(name="Sample Product 2", description="Second sample", price=20.99)
        db.session.add_all([product1, product2])
        db.session.commit()
        yield

        # Cleanup: Remove the sample data
        db.session.query(Product).filter(Product.name.in_([
            "Sample Product 1",
            "Sample Product 2"
        ])).delete(synchronize_session=False)
        db.session.commit()