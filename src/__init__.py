from flask import Blueprint
from flask_restful import Api
from src.views.News import *
from src.views.Topic import *

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(News, "/news", "/news/<int:id>")

api.add_resource(Topic, "/topic", "/topic/<int:id>")
