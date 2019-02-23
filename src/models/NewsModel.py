from ..models import db, ma
from marshmallow import fields

NewsTopic = db.Table('tbl_details', db.Model.metadata,
                    db.Column('news_id', db.Integer, db.ForeignKey('tbl_news.news_id'), primary_key=True),
                    db.Column('topic_id', db.Integer, db.ForeignKey('tbl_topics.topic_id'), primary_key=True),
                  )

class NewsModel(db.Model):
    __tablename__ = 'tbl_news'
    news_id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('tbl_news_status.status_id'))
    title = db.Column(db.String(200), unique=True)
    content = db.Column(db.Text)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    modified_date = db.Column(db.DateTime)

    statuses = db.relationship('NewsStatusModel')
    topic_list = db.relationship('TopicModel', secondary=NewsTopic, lazy='subquery',
                                 backref=db.backref('NewsTopic', lazy=True))

    def save(self, _topic_list):
        db.session.add(self)
        db.session.flush()

        for row in _topic_list:
            cmd = NewsTopic.insert().values(news_id=self.news_id, topic_id=row['topic_id'])
            db.session.execute(cmd)

        db.session.commit()

    def commit(self):
        db.session.commit()

class NewsSchema(ma.Schema):
    news_id = fields.Integer()
    status_id = fields.Integer()
    title = fields.String()
    content = fields.String()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()

    statuses = fields.Nested('NewsStatusSchema', exclude=["created_date"])
    topic_list = fields.Nested('TopicSchema', many=True, only=['topic_id', 'topic'])
