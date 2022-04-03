from flask import Flask, jsonify, Blueprint

apiProducts = Blueprint('apiProducts', __name__, url_prefix='/api/products')


@apiProducts.route('/')
def index():
    return jsonify({"success": True, "message": "Hello Products"})
