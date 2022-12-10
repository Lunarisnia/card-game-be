from src.base.PyMongoWrapper import PyMongoWrapper
import os

database = PyMongoWrapper(os.environ.get('CONNECTION_STRING'), os.environ.get('DATABASE_NAME'))