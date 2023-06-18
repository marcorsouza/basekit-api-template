from functools import wraps
from flasgger import Swagger
from flask import jsonify, request

def swagger_init_app(app):
    TEMPLATE = {
        "securityDefinitions": {
            "Bearer":
                {
                    "type": "apiKey",
                    "name": "Authorization",
                    "in": "header"
                }
        },
        "security": [
            {"Bearer": []}
        ], 
    }
    swagger = Swagger(app, template=TEMPLATE)
    return swagger