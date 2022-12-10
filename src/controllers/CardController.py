from src.base.BaseController import BaseController
from src.libs.Card import Card, Gender


class CardController(BaseController):
    def draw_card_male(self):
        card = self.model.draw_card([Gender.MALE])
        return {"gender": Gender.MALE.value, "card": card}

    def draw_card_female(self):
        card = self.model.draw_card([Gender.FEMALE])
        return {"gender": Gender.FEMALE.value, "card": card}
    
    def reset_graveyard(self):
        return self.model.reset_graveyard()

    def fetch_card_count(self):
        cards = self.model.fetch_cards([Gender.MALE, Gender.FEMALE])
        return {"count": len(cards)}


cardController = CardController(Card())
