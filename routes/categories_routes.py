from flask import Blueprint
from controllers import categories_controller

categories = Blueprint("categories", __name__)


@categories.route("/categories", methods=["GET"])
def category_get_all():
    return categories_controller.category_get_all()


@categories.route('/categories/<category_id>', methods=["GET"])
def category_get_by_id(category_id):
    return categories_controller.category_get_by_id(category_id)


@categories.route('/categories', methods=['POST'])
def category_add():
    return categories_controller.category_add()


@categories.route('/categories/<category_id>', methods=['PUT'])
def category_update(category_id):
    return categories_controller.category_update(category_id)


@categories.route("/categories/delete/<category_id>", methods=['DELETE'])
def category_delete(category_id):
    return categories_controller.category_delete(category_id)


@categories.route('/categories/activate/<category_id>', methods=['PATCH'])
def category_activate(category_id):
    return categories_controller.category_activate(category_id)


@categories.route('/categories/deactivate/<category_id>', methods=['PATCH'])
def category_deactivate(category_id):
    return categories_controller.category_deactivate(category_id)
