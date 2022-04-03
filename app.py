from flask import Flask, jsonify

from api.users import apiUsers
from api.products import apiProducts
from api.admins import apiAdmins

from ecommerce import createApp
from ecommerce.initialize_db import createDB


# APP AND DB CREATION ---------------------------------------------------------
app = createApp()
createDB()
# -----------------------------------------------------------------------------


# BLUEPRINT REGISTERS ---------------------------------------------------------
app.register_blueprint(apiUsers)
app.register_blueprint(apiProducts)
app.register_blueprint(apiAdmins)
# -----------------------------------------------------------------------------


@app.route("/")
def index():
    return jsonify({"success": True, "message": "Hello World"})


@app.route("/shares")
def shares():
    return jsonify({"success": True, "data": ["paylasim1", "paylasim2", "paylasim3"]})


@app.route("/profile")
def profile():
    return {"id": 1, "name": "Furkan", "age": 25, "following": 80, "followers": 100, "followersList": ["oguz", "alper"]}


if __name__ == "__main__":
    app.run(debug=True)
