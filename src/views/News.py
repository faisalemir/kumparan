from flask import request
from flask_restful import Resource
from ..models.NewsModel import NewsModel, NewsSchema
from ..models.NewsStatusModel import *
from ..models import DBFunc
from ..views import resFormat

newslist_schema = NewsSchema(many=True)
news_schema = NewsSchema()

class News(Resource):
    def get(self, id):
        query = NewsModel.query.join(NewsModel.topic_list).all()
        data = newslist_schema.dump(query).data

        return resFormat(200, data).set, 200

    def post(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                msg = {"message": "No input data provided"}
                return resFormat(400, msg).set, 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = NewsModel.query.filter_by(title=data['title']).first()
            if resdata:
                msg = {"message": "Title already exists"}
                return resFormat(400, msg).set, 400

            resdata = NewsModel(
                status_id=json_data['status_id'],
                title=json_data['title'],
                content=json_data['content']
            )

            DBFunc().addcommit(resdata)

            res = news_schema.dump(resdata).data
        except:
            msg = {"message": "Bad Request"}
            return resFormat(400, msg).set, 400

        return resFormat(201, res).set, 201

    def put(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                msg = {"message": "No input data provided"}
                return resFormat(400, msg).set, 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = NewsModel.query.filter_by(news_id=data['news_id']).first()
            if not resdata:
                msg = {"message": "News does not exist"}
                return resFormat(400, msg).set, 400

            resdata.status_id = data['status_id']
            resdata.title = data['title']
            resdata.content = data['content']

            DBFunc().commitaja()

            res = news_schema.dump(resdata).data
        except:
            msg = {"message": "Bad Request"}
            return resFormat(400, msg).set, 400

        return resFormat(204, res).set, 204

    def delete(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                msg = {"message": "No input data provided"}
                return resFormat(400, msg).set, 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = NewsModel.query.filter_by(news_id=data['news_id']).delete()

            DBFunc().commitaja()

            res = news_schema.dump(resdata).data
        except:
            msg = {"message": "Bad Request"}
            return resFormat(400, msg).set, 400

        return resFormat(204, res).set, 204

# class NewsParam(Resource):
#     def get(self, id):
#         query = NewsModel.query.filter_by(news_id=id).first()
#         data = news_schema.dump(query).data
#
#         return {"status": 200, "data": data}, 200