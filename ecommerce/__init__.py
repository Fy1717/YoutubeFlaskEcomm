from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()


def createApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/ecommerce"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)

    return app
