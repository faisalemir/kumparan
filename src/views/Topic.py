from flask import request
from flask_restful import Resource
from ..models.TopicModel import TopicModel, TopicSchema
from ..models import DBFunc
from ..views import resFormat

topiclist_schema = TopicSchema(many=True)
topic_schema = TopicSchema()

class Topic(Resource):
    def get(self):
        query = TopicModel.query.all()
        data = topiclist_schema.dump(query).data


        return resFormat(200, data).set, 200

    def post(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                msg = {"message": "No input data provided"}
                return resFormat(400, msg).set, 400

            data, errors = topic_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = TopicModel.query.filter_by(title=data['title']).first()
            if resdata:
                msg = {"message": "Title already exists"}
                return resFormat(400, msg).set, 400

            resdata = TopicModel(
                status_id=json_data['status_id'],
                title=json_data['title'],
                content=json_data['content']
            )

            DBFunc().addcommit(resdata)

            res = topic_schema.dump(resdata).data
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

            data, errors = topic_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = TopicModel.query.filter_by(topic_id=data['topic_id']).first()
            if not resdata:
                msg = {"message": "News does not exist"}
                return resFormat(400, msg).set, 400

            resdata.status_id = data['status_id']
            resdata.title = data['title']
            resdata.content = data['content']

            DBFunc().commitaja()

            res = topic_schema.dump(resdata).data
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

            data, errors = topic_schema.load(json_data)
            if errors:
                return resFormat(422, errors).set, 422

            resdata = TopicModel.query.filter_by(topic_id=data['topic_id']).delete()

            DBFunc().commitaja()

            res = topic_schema.dump(resdata).data
        except:
            msg = {"message": "Bad Request"}
            return resFormat(400, msg).set, 400

        return resFormat(204, res).set, 204

class TopicParam(Resource):
    def get(self, id):
        query = TopicModel.query.filter_by(topic_id=id).first()
        data = topic_schema.dump(query).data

        return {"status": 200, "data": data}, 200