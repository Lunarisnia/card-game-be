from src.base.BaseController import BaseController
from src.libs.User import User


class UserController(BaseController):
    def getUser(self, query) -> dict:
        return self.model.get(query)

    def addUser(self, data) -> dict:
        return self.model.add(data)

    def deleteUser(self, data) -> dict:
        return self.model.delete(data)

    def updateUser(self, query, update) -> dict:
        return self.model.update(query, update)


userController = UserController(User())
