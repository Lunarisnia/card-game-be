from src.base.BaseModel import BaseModel
from src.database.MongoConfig import database
from src.base.PyMongoWrapper import PyMongoUtility
from enum import Enum
from random import shuffle


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class Card(BaseModel):
    def __init__(self) -> None:
        super().__init__()
        self.col = database

    def draw_card(self, gender=[Gender.MALE]):
        cards = self.fetch_cards(gender)
        if len(cards) < 1: return None
        shuffle(cards)
        drawn_card = cards.pop()
        self.put_card_away(drawn_card['_id'])
        return PyMongoUtility(drawn_card).to_json()

    def put_card_away(self, card_id):
        self.col.get_collection('graveyard').insert_one({"card_id": card_id})

    def fetch_cards(self, gender=[Gender.MALE]):
        graveyard = self.fetch_graveyard()
        cards = self.col.get_collection('cards').find(
            {"_id": {"$nin": [body['card_id'] for body in graveyard]}, "gender": {"$in": [g.value for g in gender]}}).to_python()
        return cards

    def fetch_graveyard(self):
        return self.col.get_collection('graveyard').find().to_python()

    def reset_graveyard(self):
        graveyard = self.fetch_graveyard()
        self.col.delete_many({"_id": {"$in": [body['_id'] for body in graveyard]}})
        return {"message": "Graveyard is reset!"}
