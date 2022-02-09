from flask import Flask, jsonify, request

from flask_pymongo import PyMongo
from oncase.exceptions.api_exception import APIException


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/oncase"
mongo = PyMongo(app)


def execute(requestData):
    print(requestData)
    user = mongo.db.user.insert_one(requestData)

    if user:
        return jsonify(user)
    else:
        raise APIException(
            message="An error occured on insertion", status_code=400)
