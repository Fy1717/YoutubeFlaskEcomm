from flask import Flask, jsonify, Blueprint

apiUsers = Blueprint('apiUser', __name__, url_prefix='/api/users')


@apiUsers.route('/')
def users():
    allUsers = [{"id": 1, "name": "furkan", "surname": "yildiz", "age": 25},
                {"id": 2, "name": "oguz", "surname": "demir", "age": 25},
                {"id": 3, "name": "alper", "surname": "yurtseven", "age": 23}]

    return jsonify({"success": True, "data": allUsers})


@apiUsers.route("/<int:id>")
def user(id):
    user = {"id": 2, "name": "oguz", "surname": "demir", "age": 25}

    return jsonify({"success": True, "data": user})
