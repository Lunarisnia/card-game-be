from flask import Flask
from src.base.FlaskAppWrapper import FlaskAppWrapper
from src.routes.index import routes

flask_app = Flask(__name__)
app = FlaskAppWrapper(flask_app)

index_route = routes
for route in index_route:
    app.add_endpoint(**route)