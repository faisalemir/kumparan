from ..models import db, ma
from marshmallow import fields

details = db.Table('tbl_details',
                    db.Column('news_id', db.Integer, db.ForeignKey('tbl_news.news_id'), primary_key=True),
                    db.Column('topic_id', db.Integer, db.ForeignKey('tbl_topics.topic_id'), primary_key=True),
                    db.PrimaryKeyConstraint('news_id', 'topic_id')
                  )

class NewsModel(db.Model):
    __tablename__ = 'tbl_news'
    news_id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('tbl_news_status.status_id'))
    title = db.Column(db.String(200), unique=True)
    content = db.Column(db.Text)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime)

    topic_list = db.relationship('TopicModel', secondary=details, lazy='subquery', backref=db.backref('tbl_topics', lazy=True))

class NewsSchema(ma.Schema):
    news_id = fields.Integer()
    status_id = fields.Integer()
    title = fields.String()
    content = fields.String()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()

class TopicModel(db.Model):
    __tablename__ = 'tbl_topics'
    topic_id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200))
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime)

    news_list = db.relationship('NewsModel', secondary=details, lazy='subquery', backref=db.backref('tbl_news', lazy=True))

class TopicSchema(ma.Schema):
    topic_id = fields.Integer()
    topic = fields.String()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()