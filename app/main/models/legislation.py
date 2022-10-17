# legislation.py

from flask import Flask, request, jsonify
from typing import List, Optional, Union, Any
from flask_mongoengine import MongoEngine
from fastapi.encoders import jsonable_encoder
from bs4 import BeautifulSoup
from pydantic.dataclasses import dataclass

app = Flask(__name__)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'userdb',
#     'host': 'localhost',
#     'port': 27017
# }
#
# db = MongoEngine()
# db.init_app(app)

@dataclass
class LegislationModel(object):
    LegislationVersionId: int
    LegislationSourceId: str
    LegislationVersionOrdinal: int
    Title: str
    NativeTitle: Optional[str]
    JurisdictionSourceId: str
    JurisdictionName: str
    IssuingBodySourceId: str
    IssuingBodyName: str
    PartVersionId: int
    PartSourceId: str
    PartVersionOrdinal: int
    OrderNum: int
    Content: str
    NativeContent: Optional[str]
    ParentPartVersionId: int
    ParentPartSourceId: str
    ParentPartVersionOrdinal: int

    # def __init__(self, NativeTitle=None, NativeContent=None):
    #     self.NativeContent = NativeContent
    #     self.NativeTitle = NativeTitle
    #
    # def __init__(self):
    #     self

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.__dict__
        #data = self.dict(by_alias=True, exclude_none=True)
        title_data = BeautifulSoup(data["Title"], 'html.parser').get_text()
        content_data = BeautifulSoup(data["Content"], 'html.parser').get_text()
        data["Content"] = content_data
        data["Title"] = title_data
        #updated_dict = {k:v for k,v in data.items() if v is not None}
        return data

