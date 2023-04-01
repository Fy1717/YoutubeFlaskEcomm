from ecommerce.models import Category
from flask import Flask, jsonify, Blueprint, request

apiCategories = Blueprint("apiCategories", __name__,
                          url_prefix="/api/categories")


@apiCategories.route("/")
def categories():
    try:
        allCategories = Category.get_all_categories()
        categories = []

        print("allCategories : ", allCategories)

        for category in allCategories:
            categories.append({"id": category.id, "name": category.name})

        return jsonify({"success": True, "data": categories, "count": len(categories)})
    except Exception as e:
        print("ERROR IN CATEGORIES: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiCategories.route("/addCategory", methods=["POST"])
def addCategory():
    try:
        name = request.form.get("name")

        if name == None:
            return jsonify({"success": False, "message": "Name is required"})

        Category.add_category(name)

        return jsonify({"success": True, "message": "Category added successfully"})
    except Exception as e:
        print("ERROR in add_admin: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiCategories.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def category(id):
    try:
        category = Category.get_category_by_id(id)

        if category is None:
            return jsonify({"success": False, "message": "Category not found"})

        if request.method == "GET":
            categoryObj = {"id": category.id, "name": category.name}

            return jsonify({"success": True, "data": categoryObj})

        # -----------------------------------------------------------------------------

        elif request.method == "DELETE":
            Category.delete_category(id)

            return jsonify({"success": True, "message": "Category deleted"})

        # -----------------------------------------------------------------------------

        elif request.method == "PUT":
            name = request.form.get("name")

            print("NAME: ", name)

            if name == None:
                name = category.name

            Category.update_category(id, name)

            return jsonify({"success": True, "message": "Category updated"})

        # -----------------------------------------------------------------------------

    except Exception as e:
        print("ERROR in category: ", e)
        return jsonify({"success": False, "message": "There is an error.."})
