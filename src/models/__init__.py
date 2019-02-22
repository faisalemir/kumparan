from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class DBFunc:
    def addcommit(self, data):
        db.session.add(data)
        db.session.commit()

    def commitaja(self):
        db.session.commit()

