from ..models import db, ma
from marshmallow import fields

class NewsModel(db.Model):
    __tablename__ = 'tbl_news'
    news_id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer)
    title = db.Column(db.String(200), unique=True)
    content = db.Column(db.Text)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime)
    # news_status = db.relationship('NewsStatusModel', backref=db.backref('news', lazy='dynamic' ))

class NewsSchema(ma.Schema):
    news_id = fields.Integer()
    status_id = fields.Integer()
    title = fields.String()
    content = fields.String()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()