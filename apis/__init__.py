from flask import Blueprint
from flask_restx import Api
from .status import api as status_ns
from .prediction_ns import api as class_prediction_ns

blueprint = Blueprint("api",__name__)

api = Api(
    blueprint,
    title = "Text based classification Api Serving",
    version = "1",
    description = "Api for IKYC Factory Document classification",
)
api.add_namespace(class_prediction_ns)
api.add_namespace(status_ns)
