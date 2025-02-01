from flask import Blueprint, jsonify, request
from app.models import Product
from app.db import db

bp = Blueprint('routes', __name__)

@bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products])

@bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price})

@bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(name=data['name'], description=data.get('description', ''), price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price}), 201

@bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.description = data.get('description', product.description)
    product.price = data['price']
    db.session.commit()
    return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price})

@bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"})

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})
