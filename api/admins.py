from flask import Flask, jsonify, Blueprint

apiAdmins = Blueprint("apiAdmins", __name__, url_prefix="/api/admins")


@apiAdmins.route("/")
def index():
    return jsonify({"success": True, "message": "Hello Admins"})
