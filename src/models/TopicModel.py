from ..models import db, ma
from marshmallow import fields
from ..models.NewsTopic import NewsTopic

class TopicModel(db.Model):
    __tablename__ = 'tbl_topics'
    topic_id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200))
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime)

    news_list = db.relationship('NewsModel', secondary=NewsTopic, lazy='subquery', back_populates='topic_list')

class TopicSchema(ma.Schema):
    topic_id = fields.Integer()
    topic = fields.String()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()

    news_list = fields.Nested('NewsSchema', exclude=('topic_list',), many=True)