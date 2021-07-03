from flask import request
from flask_restx import Namespace,Resource,fields
api = Namespace("status",description = "Namespace for API health status")

@api.route("/isup")
class IsHealthy(Resource):
    def get(self):
        return {
            "success": "The Api is up and running"
            "remote_ip_address":str(request.remote_addr)
        }