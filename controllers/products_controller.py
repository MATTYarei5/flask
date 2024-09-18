from flask import jsonify, request
from data import product_records


def return_string(number):
    return f"your number is {number}."


def get_json_stuff():
    return jsonify({"color": "red", "number": 2})


def product_get_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            return jsonify({"message": "products found", "results": product}), 200
    return jsonify({"message": f'Product with id {product_id} not found.'}), 404


def product_update(product_id):
    post_data = request.form or request.json

    product_id = post_data.get("product_id")
    for product in product_records:
        if product['product_id'] == int(product_id):
            return jsonify(product), 200
    return jsonify({"message": f'Product with id {product_id} not found.'}), 400


def product_add():
    post_data = request.json

    product_records.append(post_data)
    return jsonify({"message": "record added", "result": post_data}), 201


def product_delete(product_id):
    for product in product_records:
        if product["product_id"] == int(product_id):
            product_records.remove(product)

    return jsonify({"message": "product deleted"}), 200
