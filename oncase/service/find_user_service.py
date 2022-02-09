from flask import Flask, jsonify, request

from flask_pymongo import PyMongo
from oncase.util.mongo_engine_json_encoder import parse_json
from oncase.exceptions.api_exception import APIException

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/oncase"
mongo = PyMongo(app)


def execute(requestData):
    user = parse_json(mongo.db.user.find_one(requestData))

    if user:
        return jsonify(user)
    else:
        raise APIException(message="User not found", status_code=404)
