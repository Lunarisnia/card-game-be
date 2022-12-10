from pymongo import MongoClient, cursor
from bson import ObjectId, json_util
import json

class PyMongoUtility():
    def __init__(self, document=None):
        self.document = document

    def to_python(self):
        if type(self.document) is cursor.Cursor:
            return list(self.document)
        else:
            return self.document
    
    def to_json(self):
        return json.loads(json_util.dumps(self.document))

    # Help Generate Object Id
    def ObjectId(self, text):
        return ObjectId(text)

class PyMongoWrapper():
    def __init__(self, connection_string, database) -> None:
        self.connection_string = connection_string
        self.connection = MongoClient(connection_string)[database]
        self.collection = self.connection

    def get_collection(self, collection):
        self.collection = self.connection[collection]
        return self

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def find(self, query={}):
        return PyMongoUtility(self.collection.find(query))

    def find_one(self, query={}):
        return PyMongoUtility(self.collection.find_one(query))

    def delete_many(self, query={}):
        return self.collection.delete_many(query)