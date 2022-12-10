from src.base.BaseModel import BaseModel


class User(BaseModel):
    def get(self, query):
        super().get(query)
        return {"query": query, "data": [{"name": "Aan"}]}

    def add(self, data):
        return {"data": [{"name": "Aan"}, data]}

    def update(self, query, update):
        assert query != None
        return {"data": [update]}

    def delete(self, query):
        assert query != None
        return {"data": []}
