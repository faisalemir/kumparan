from ..models import db, ma
from marshmallow import fields

class NewsStatusModel(db.Model):
    __tablename__ = 'tbl_news_status'
    status_id = db.Column(db.Integer, primary_key=True)
    news_status = db.Column(db.String(20))
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

class NewsStatusSchema(ma.Schema):
    status_id = fields.Integer()
    news_status = fields.String()
    created_date = fields.DateTime()