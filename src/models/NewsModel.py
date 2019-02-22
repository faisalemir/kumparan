from ..models import db, ma
from marshmallow import fields
from ..models.NewsTopic import NewsTopic

class NewsModel(db.Model):
    __tablename__ = 'tbl_news'
    news_id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('tbl_news_status.status_id'))
    title = db.Column(db.String(200), unique=True)
    content = db.Column(db.Text)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime)

    statuses = db.relationship('NewsStatusModel')
    topic_list = db.relationship('TopicModel', secondary=NewsTopic, lazy='subquery',  back_populates='news_list')

class NewsSchema(ma.Schema):
    news_id = fields.Integer()
    status_id = fields.Integer()
    title = fields.String()
    content = fields.String()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()

    statuses = fields.Nested('NewsStatusSchema')
    topic_list = fields.Nested('TopicSchema', exclude=('news_list',), many=True)
