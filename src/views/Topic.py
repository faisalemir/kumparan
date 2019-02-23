from flask import request
from flask_restful import Resource
from ..models.TopicModel import TopicModel, TopicSchema
from ..views import resFormat

topiclist_schema = TopicSchema(many=True)
topic_schema = TopicSchema()

class Topic(Resource):
    def get(self, id=None):
        if id is None:
            query = TopicModel.query.all()
            data = topiclist_schema.dump(query).data
        else:
            query = TopicModel.query.filter_by(topic_id=id).first()
            data = topic_schema.dump(query).data

        return resFormat(200, data), 200

    def post(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                msg = {"message": "No input data provided"}
                return resFormat(400, msg), 400

            data, errors = topic_schema.load(json_data)
            if errors:
                return resFormat(422, errors), 422

            model = TopicModel(
                topic=json_data["topic"]
            )

            model.save()

            res = topic_schema.dump(model).data
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

            data, errors = topic_schema.load(json_data)
            if errors:
                return resFormat(422, errors), 422

            model = TopicModel()
            resdata = model.query.filter_by(topic_id=data['topic_id']).first()
            if not resdata:
                msg = {"message": "News does not exist"}
                return resFormat(400, msg), 400

            resdata.topic = data['topic']

            model.commit()

            res = topic_schema.dump(model).data
        except Exception as e:
            msg = {"message": str(e)}
            return resFormat(400, msg), 400

        return resFormat(200, res), 200

    def delete(self, id=None):
        try:
            model = TopicModel()
            resdata = model.query.filter_by(topic_id=id).delete()

            model.commit()

            res = topic_schema.dump(model).data
        except Exception as e:
            msg = {"message": str(e)}
            return resFormat(400, msg), 400

        return resFormat(204, res), 204