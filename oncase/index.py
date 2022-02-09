from flask import Flask, jsonify, request

from flask_pymongo import PyMongo
from oncase.service import find_all_users_service, find_user_service, insert_user_service
from oncase.exceptions import api_exception

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/oncase"
mongo = PyMongo(app)


@app.errorhandler(api_exception.APIException)
def default_api_exception(error):
    return jsonify({"error": error.message}), error.status_code


@app.route('/user', methods=['POST'])
def add_user():
    return insert_user_service.execute(request.get_json())


@app.route('/user/<string:userId>', methods=['GET'])
def find_user_by_id(userId):
    return find_user_service.execute({"_id": userId})


@app.route('/users', methods=['GET'])
def find_users():
    return find_all_users_service.execute()


if __name__ == "__main__":
    app.run()
