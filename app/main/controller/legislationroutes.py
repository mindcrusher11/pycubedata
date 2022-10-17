# Configure Flask & Flask-PyMongo:
from flask import Flask, jsonify, request
from pymongo.errors import DuplicateKeyError

from app.main.models.legislation import LegislationModel
from app.main.service.mongoops import MongoOps
from app.main.service.readfile import ReadFile

app = Flask(__name__)

mongoops = MongoOps()


@app.errorhandler(404)
def resource_not_found(e):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e):
    """
    An error-handler to ensure that MongoDB duplicate key errors are returned as JSON.
    """
    return jsonify(error=f"Duplicate key error."), 400


@app.route("/legislation/add", methods=["POST"])
def add_legislation():
    legislation_json = request.get_json()
    legislation = LegislationModel(**legislation_json)
    MongoOps.save(legislation)
    return legislation


@app.route("/legislation/find", methods=["GET"])
def find_legislation():
    legislation_json = request.get_json()
    legislation = LegislationModel(**legislation_json)
    return MongoOps.read(legislation)


@app.route("/legislation/delete", methods=["GET"])
def delete_legislation():
    legislation_json = request.get_json()
    legislation = LegislationModel(**legislation_json)
    MongoOps.delete(legislation)
    return legislation


@app.route("/legislation/loadfile", methods=["GET"])
def read_file():
    args = request.args
    file_path = args.get("path")
    readfile = ReadFile()
    legislation_json = readfile.readjson(file_path)
    legislation = [LegislationModel(**k) for k in legislation_json]

    [mongoops.save(leg.to_bson()) for leg in legislation]
    return '', 201

@app.route("/legislation/search", methods=["GET"])
def search_legislation():
    args = request.args
    search_text = args.get("searchtext")
    cursor = mongoops.search(search_text)
    return {"data" : [LegislationModel(**doc).to_json() for doc in cursor] }, 200


if __name__ == '__main__':
    app.run(debug=True)
