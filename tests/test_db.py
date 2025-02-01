from app.db import db
from sqlalchemy.sql import text
from app.models import Product

def test_database_connection(app):
    """
    Test that the database connection works by executing a simple query.
    """
    with app.app_context():
        with db.engine.connect() as connection:
            # Use text() to make the query executable
            result = connection.execute(text("SELECT 1")).scalar()
            assert result == 1


def test_sample_data(sample_data, app):
    """
    Test that the sample data is correctly added to the database.
    """
    with app.app_context():
        # Query the Product model to check if sample data exists
        product1 = Product.query.filter_by(name="Sample Product 1").first()
        product2 = Product.query.filter_by(name="Sample Product 2").first()

        assert product1 is not None
        assert product1.description == "First sample"
        assert product1.price == 10.99

        assert product2 is not None
        assert product2.description == "Second sample"
        assert product2.price == 20.99
