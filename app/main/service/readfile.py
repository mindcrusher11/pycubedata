import json

from bs4 import BeautifulSoup

from app.main.iservice.ireadfile import IReadFile


class ReadFile(IReadFile):

    def readjson(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.loads(f.read())
            return json_data

    def readxml(self, file_path):
        file = open(file_path, "r")
        contents = file.read()
        soup = BeautifulSoup(contents, 'xml')
