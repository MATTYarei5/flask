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


@categories.route('/categories/<category_id>/<status>', methods=['PATCH'])
def category_update_status(category_id, status):
    if status not in ['activate', 'deactivate']:
        return "Invalid status. Must be either 'activate' or 'deactivate'.", 400
    return categories_controller.category_update_status(category_id, status)


@categories.route('/categories/active', methods=['GET'])
def category_get_all_active():
    return categories_controller.category_get_all_active()
