class BaseModel:
    def __init__(self) -> None:
        pass
    
    def add(self, data):
        return "Create a new data"

    def get(self, query):
        return "Fetch a Data"

    def update(self, query, update):
        return "Update a Data"

    def delete(self, query):
        return "Delete a Data"