from flask import request
from flask_restful import Resource, reqparse
from ..models.NewsModel import NewsModel, NewsSchema, NewsTopic
from ..models.TopicModel import TopicModel
from ..models.NewsStatusModel import *
from ..views import resFormat

newslist_schema = NewsSchema(many=True)
news_schema = NewsSchema()

class News(Resource):
    def get(self, id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('status', type=int)
        parser.add_argument('topic', type=int)
        args = parser.parse_args()

        stat = args.get('status')
        top = args.get('topic')

        #filter by news status
        stats = lambda q:  q.filter(NewsModel.status_id == stat) if stat is not None else q

        #filter by topic
        tops = lambda q:  q.filter(NewsModel.topic_list.any(TopicModel.topic_id.like(top))) if top is not None else q

        if id is None:
            query = NewsModel.query
            query = stats(query)
            query = tops(query)
            data = newslist_schema.dump(query.all()).data
        else:
            query = NewsModel.query.filter_by(news_id=id)
            query = stats(query)
            query = tops(query)
            data = news_schema.dump(query.first()).data

        return resFormat(200, data), 200

    def post(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                msg = {"message": "No input data provided"}
                return resFormat(400, msg), 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors), 422

            resdata = NewsModel.query.filter_by(title=data['title']).first()
            if resdata:
                msg = {"message": "Title already exists"}
                return resFormat(400, msg), 400

            model = NewsModel(
                status_id=json_data['status_id'],
                title=json_data['title'],
                content=json_data['content']
            )

            model.save(json_data['topic_list'])

            res = news_schema.dump(model).data
        except Exception as e:
            msg = {"message": str(e)}
            return resFormat(400, msg), 400

        return resFormat(201, res), 201

    def put(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                msg = {"message": "No input data provided"}
                return resFormat(400, msg), 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors), 422

            model = NewsModel()
            resdata = model.query.filter_by(news_id=data['news_id']).first()
            if not resdata:
                msg = {"message": "News does not exist"}
                return resFormat(400, msg), 400

            resdata.status_id = data['status_id']
            resdata.title = data['title']
            resdata.content = data['content']

            model.commit()

            res = news_schema.dump(model).data
        except Exception as e:
            msg = {"message": str(e)}
            return resFormat(400, msg), 400

        return resFormat(200, res), 200

    def delete(self, id=None):
        try:
            model = NewsModel()
            resdata = model.query.filter_by(news_id=id).delete()

            model.commit()

            res = news_schema.dump(model).data
        except Exception as e:
            msg = {"message": str(e)}
            return resFormat(400, msg), 400

        return resFormat(204, res), 204