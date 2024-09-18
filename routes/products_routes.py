from flask import Blueprint
from controllers import products_controller


products = Blueprint("products", __name__)


@products.route("/return-string/<number>")
def return_string(number):
    return products_controller.return_string(number)


@products.route("/json-stuff")
def get_json_stuff():
    return products_controller.get_json_stuff()


@products.route('/products/<product_id>', methods=["GET"])
def product_get_by_id(product_id):
    return products_controller.product_get_by_id(product_id)


@products.route('/product/update', methods=['PUT'])
def product_update(product_id):
    return products_controller.product_update(product_id)


@products.route("/product", methods=['POST'])
def product_add():
    return products_controller.product_add()


@products.route("/product/delete/<product_id>", methods=['DELETE'])
def product_delete(product_id):
    return products_controller.product_delete(product_id)
