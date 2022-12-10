from src.base.BaseRouter import BaseRouter
from src.controllers.UserController import userController
from flask import request

class HomeRouter(BaseRouter):
    def getUser():
        query_name = request.args.get("name")
        return userController.getUser(query=query_name)

    def addUser():
        user_data = request.json
        return userController.addUser(user_data)

    def deleteUser():
        user_data = request.json
        return userController.deleteUser(user_data)

    def updateUser():
        body = request.json
        return userController.updateUser(body['name'], body['update'])