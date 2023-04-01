from ecommerce.models import Product
from flask import Flask, jsonify, Blueprint, request

apiProducts = Blueprint("apiProducts", __name__, url_prefix="/api/products")


@apiProducts.route("/")
def products():
    try:
        allProducts = Product.get_all_products()
        products = []

        for product in allProducts:
            products.append(
                {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "oldPrice": product.oldPrice,
                    "description": product.description,
                    "category_id": product.category_id,
                }
            )

        return jsonify({"success": True, "data": products, "count": len(products)})

    except Exception as e:
        print("ERROR IN PRODUCTS: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiProducts.route("/addProduct", methods=["POST"])
def addproduct():
    try:
        name = request.form.get("name")
        price = request.form.get("price")
        oldPrice = request.form.get("oldPrice")
        description = request.form.get("description")
        category_id = request.form.get("categoryId")

        if name == None:
            return jsonify({"success": False, "message": "Name is required"})
        if price == None:
            return jsonify({"success": False, "message": "Price is required"})
        if oldPrice == None:
            oldPrice = price
        if description == None:
            return jsonify({"success": False, "message": "Description is required"})
        if category_id == None:
            return jsonify({"success": False, "message": "Category is required"})

        Product.add_product(name, price, oldPrice, description, category_id)

        return jsonify({"success": True, "message": "Product added successfully"})
    except Exception as e:
        print("ERROR in add_admin: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiProducts.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def product(id):
    try:
        product = Product.get_product_by_id(id)

        if product is None:
            return jsonify({"success": False, "message": "Product not found"})

        if request.method == "GET":
            productObj = {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "oldPrice": product.oldPrice,
                "description": product.description,
                "category_id": product.category_id,
            }

            return jsonify({"success": True, "data": productObj})

        # -----------------------------------------------------------------------------

        elif request.method == "DELETE":
            Product.delete_product(id)

            return jsonify({"success": True, "message": "product deleted"})

        # -----------------------------------------------------------------------------

        elif request.method == "PUT":
            name = request.form.get("name")
            price = request.form.get("price")
            oldPrice = request.form.get("oldPrice")
            description = request.form.get("description")
            category_id = request.form.get("categoryId")

            if name == None:
                name = product.name
            if price == None:
                price = product.price
            if oldPrice == None:
                oldPrice = product.oldPrice
            if description == None:
                description = product.description
            if category_id == None:
                category_id = product.category_id

            Product.update_product(
                id, name, price, oldPrice, description, category_id)

            return jsonify({"success": True, "message": "product updated"})

        # -----------------------------------------------------------------------------

    except Exception as e:
        print("ERROR in product: ", e)
        return jsonify({"success": False, "message": "There is an error.."})
