import logging
from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

logging.basicConfig(filename=f"log/test", encoding="utf-8", level=logging.INFO)


class Image(Resource):
    def post(self):
        """Given an image file in request body, return an audio.mp3 file"""
        logging.info(request.json)
        return "post"

    def get(self):
        logging.info(request.json)
        return "Hello, World", 200


api.add_resource(Image, "/image", "/")
