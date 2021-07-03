from flask_restx import Namespace, Resource, fields,Api
from core.prediction import *
api = Namespace(
    "class-prediction",
    description = "IKYC Factory Document Classification",
)

input_payload = api.model(
    "InputModel",
    {
        "text": fields.String(
            required = True, description = "raw msocr of the files"
        ),
    },
)

model = api.model("Model",{
    "text": fields.String,
    "class": fields.String
})

@api.route("/")
@api.expect(input_payload)
class Prediction(Resource):
    @api.marshal_with(model,envelop = "resource")
    @api.response(201,"Success")
    @api.response(500,"Internal Server Error")
    @api.response(404,"Not Found")
    def post(self):
        text_file = api.payload['text']
        with open("./assets/input.txt",'w+') as f:
            f.write(text_file)
            f.close()
        response = get_prediction(config['file_path'])

        return response