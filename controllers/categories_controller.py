from flask import jsonify, request
from data import category_records


def categories_get_all():
    return jsonify({"categories": category_records}), 200


def category_get_by_id(category_id):
    for category in category_records:
        if category['category_id'] == category_id:
            return jsonify({"message": "Category found", "result": category}), 200
    return jsonify({"message": f'Category with id {category_id} not found.'}), 404


def category_add():
    post_data = request.json
    category_records.append(post_data)
    return jsonify({"message": "Category added", "result": post_data}), 201


def category_update(category_id):
    post_data = request.json
    for category in category_records:
        if category['category_id'] == category_id:
            category.update(post_data)
            return jsonify({"message": "Category updated", "result": category}), 200
    return jsonify({"message": f'Category with id {category_id} not found.'}), 404


def category_delete(category_id):
    global category_records
    category_records = [category for category in category_records if category["category_id"] != category_id]
    return jsonify({"message": "Category deleted"}), 200


def category_activity(category_id):
    for category in category_records:
        if category['category_id'] == category_id:
            category['active'] = not category["active"]
            if category["active"]:
                return jsonify({"message": "Category activated", "result": category}), 200
            return jsonify({"message": "Category deactivated", "result": category}), 200
    return jsonify({"message": f'Category with id {category_id} not found.'}), 404


def categories_get_all_active():
    active_categories = [category for category in category_records if category['active']]
    return jsonify({"active_categories": active_categories}), 200
