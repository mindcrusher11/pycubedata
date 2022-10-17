from typing import TypeVar

from flask_mongoengine import MongoEngine

from app.main.iservice.idbops import DBOps
import os

from pymongo.collection import Collection, ReturnDocument

import flask
from flask import Flask, request, url_for, jsonify
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError


T = TypeVar("T")

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/legi"
#
# db = MongoEngine()
# db.init_app(app)
pymongo = PyMongo(app)

legislation: Collection = pymongo.db.legislation
legislation.create_index([('Title',"text"), ('Content', "text")])


class MongoOps(DBOps):

    def read(self, data):
        return legislation.find(data)

    def save(self, data):
         legislation.insert_one(data)

    def update(self, data):
        legislation.find_one_and_update(data)

    def delete(self, data):
        legislation.delete_one(data)

    def search(self, search_text):
        return  legislation.find({"$text": {"$search": search_text}},{"_id":0, "__initialised__":0})
