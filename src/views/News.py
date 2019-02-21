from flask import request
from flask_restful import Resource
from ..models.NewsModel import *
from ..models import DBFunc
from ..views import resFormat

newslist_schema = NewsSchema(many=True)
news_schema = NewsSchema()

class News(Resource):
    def get(self):
        query = NewsModel.query.all()
        data = newslist_schema.dump(query).data


        return resFormat(200, data).set, 200

    def post(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                return resFormat(400, {"message": "No input data provided"}).set, 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = NewsModel.query.filter_by(title=data['title']).first()
            if resdata:
                return resFormat(400, {"message": "Title already exists"}).set, 400

            resdata = NewsModel(
                status_id=json_data['status_id'],
                title=json_data['title'],
                content=json_data['content']
            )

            DBFunc().addcommit(resdata)

            res = news_schema.dump(resdata).data
        except:
            return resFormat(400, {"message": "Bad Request"}).set, 400

        return resFormat(201, res).set, 201

    def put(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                return resFormat(400, {"message": "No input data provided"}).set, 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = NewsModel.query.filter_by(news_id=data['news_id']).first()
            if not resdata:
                return resFormat(400, {"message": "News does not exist"}).set, 400

            resdata.status_id = data['status_id']
            resdata.title = data['title']
            resdata.content = data['content']

            DBFunc().commitaja()

            res = news_schema.dump(resdata).data
        except:
            return resFormat(400, {"message": "Bad Request"}).set, 400

        return resFormat(204, res).set, 204

    def delete(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                return resFormat(400, {"message": "No input data provided"}).set, 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = NewsModel.query.filter_by(news_id=data['news_id']).delete()

            DBFunc().commitaja()

            res = news_schema.dump(resdata).data
        except:
            return resFormat(400, {"message": "Bad Request"}).set, 400

        return resFormat(204, res).set, 204

class NewsParam(Resource):
    def get(self, id):
        query = NewsModel.query.filter_by(news_id=id).first()
        data = news_schema.dump(query).data

        return {"status": 200, "data": data}, 200