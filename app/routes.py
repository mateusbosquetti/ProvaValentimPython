from flask import Blueprint, request, jsonify, render_template
from . import db
from .models import Product, product_schema, products_schema


product_bp = Blueprint('products', __name__, url_prefix='/api/products')

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        name=data['name'],
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    product.name = data['name']
    product.price = data['price']
    product.stock = data['stock']
    db.session.commit()
    return product_schema.jsonify(product)

@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
