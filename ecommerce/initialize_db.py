from ecommerce.models import db
from ecommerce import createApp


def createDB():
    app = createApp()
    with app.app_context():
        db.create_all()
