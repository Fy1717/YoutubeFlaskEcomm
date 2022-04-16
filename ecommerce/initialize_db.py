from ecommerce.models import db
from ecommerce import createApp


def createDB():
    db.create_all(app=createApp())
