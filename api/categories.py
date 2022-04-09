from flask import Flask, jsonify, Blueprint

apiCategories = Blueprint('apiCategories', __name__, url_prefix='/api/categories')


@apiCategories.route('/')
def categories():
    # veritabanından kategorileri çek
    

    return jsonify({"success": True, "data": "Hello Categories"})
