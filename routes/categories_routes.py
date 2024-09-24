from flask import Blueprint
from controllers import categories_controller

categories = Blueprint("categories", __name__)


@categories.route("/categories", methods=["GET"])
def categories_get_all():
    return categories_controller.categories_get_all()


@categories.route('/category/<category_id>', methods=["GET"])
def category_get_by_id(category_id):
    return categories_controller.category_get_by_id(category_id)


@categories.route('/category', methods=['POST'])
def category_add():
    return categories_controller.category_add()


@categories.route('/category/<category_id>', methods=['PUT'])
def category_update(category_id):
    return categories_controller.category_update(category_id)


@categories.route("/category/delete/<category_id>", methods=['DELETE'])
def category_delete(category_id):
    return categories_controller.category_delete(category_id)


@categories.route('/category/<category_id>', methods=['PATCH'])
def category_activity(category_id):
    return categories_controller.category_activity(category_id)


@categories.route('/categories/active', methods=['GET'])
def categories_get_all_active():
    return categories_controller.categories_get_all_active()
