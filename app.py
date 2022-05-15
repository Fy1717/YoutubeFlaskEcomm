from flask import Flask, jsonify
from flask_cors import CORS

from api.users import apiUsers
from api.products import apiProducts
from api.admins import apiAdmins
from api.categories import apiCategories

from ecommerce import createApp
from ecommerce.initialize_db import createDB


# APP AND DB CREATION ---------------------------------------------------------
app = createApp()
CORS(app)
createDB()
# -----------------------------------------------------------------------------


# BLUEPRINT REGISTERS ---------------------------------------------------------
app.register_blueprint(apiUsers)
app.register_blueprint(apiProducts)
app.register_blueprint(apiAdmins)
app.register_blueprint(apiCategories)
# -----------------------------------------------------------------------------


@app.route("/")
def index():
    return jsonify({"success": True, "message": "Main Page"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
