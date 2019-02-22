from ..models import db

NewsTopic = db.Table('tbl_details',
                    db.Column('news_id', db.Integer, db.ForeignKey('tbl_news.news_id'), primary_key=True),
                    db.Column('topic_id', db.Integer, db.ForeignKey('tbl_topics.topic_id'), primary_key=True),
                    db.PrimaryKeyConstraint('news_id', 'topic_id')
                  )
