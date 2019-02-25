from flask import current_app, request, url_for
from flask_restful import Resource
from ..models.NewsModel import NewsModel, NewsSchema
from ..models.TopicModel import TopicModel
from ..models.NewsStatusModel import *
from ..views import resFormat
from werkzeug.urls import url_encode

newslist_schema = NewsSchema(many=True)
news_schema = NewsSchema()

class News(Resource):
    def get(self, id=None):
        nav = None

        stat = request.args.get('status', None, type=int)
        top = request.args.get('topic', None, type=int)
        page = request.args.get('page', 1, type=int)

        #filter by news status
        stats = lambda q:  q.filter(NewsModel.status_id == stat) if stat is not None else q

        #filter by topic
        tops = lambda q:  q.filter(NewsModel.topic_list.any(TopicModel.topic_id.like(top))) if top is not None else q

        if id is None:
            per_page = current_app.config['PER_PAGE']
            args_next = request.args.copy()
            args_prev = request.args.copy()

            query = NewsModel.query
            query = stats(query)
            query = tops(query)
            query = query.order_by(NewsModel.created_date.desc())
            query = query.paginate(page, per_page, False)

            args_next['page'] = query.next_num
            args_prev['page'] = query.prev_num

            nav = {
                'per_page': per_page,
                'next': url_for(request.endpoint, **args_next) if query.has_next else None,
                'prev': url_for(request.endpoint, **args_prev) if query.has_prev else None
            }

            data = newslist_schema.dump(query.items).data
        else:
            query = NewsModel.query.filter_by(news_id=id).first()
            if not query:
                msg = {"message": "News does not exist"}
                return resFormat(404, msg), 404

            data = news_schema.dump(query).data

        return resFormat(200, data, nav), 200

    def post(self):
        try:
            json_data = request.get_json(force=True)

            if not json_data:
                msg = {"message": "No input data provided"}
                return resFormat(400, msg), 400

            data, errors = news_schema.load(json_data)
            if errors:
                return resFormat(422, errors), 422

            tmpdata = NewsModel.query.filter_by(title=data['title']).first()
            if tmpdata:
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

            model = NewsModel.query.filter_by(news_id=data['news_id']).first()
            if not model:
                msg = {"message": "News does not exist"}
                return resFormat(400, msg), 400

            model.status_id = data['status_id']
            model.title = data['title']
            model.content = data['content']

            model.commit()

            res = news_schema.dump(model).data
        except Exception as e:
            msg = {"message": str(e)}
            return resFormat(400, msg), 400

        return resFormat(200, res), 200

    def delete(self, id=None):
        try:
            model = NewsModel()
            model.query.filter_by(news_id=id).delete()

            model.commit()

            res = news_schema.dump(model).data
        except Exception as e:
            msg = {"message": str(e)}
            return resFormat(400, msg), 400

        return resFormat(204, res), 204