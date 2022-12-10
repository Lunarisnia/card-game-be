from src.base.BaseRouter import BaseRouter
from src.controllers.CardController import cardController
from flask import request, Response

class CardRouter(BaseRouter):
    def draw_card():
        try:
            gender = request.args.get('gender')
            assert gender != None
            if gender == 'm':
                return cardController.draw_card_male()
            elif gender == 'f':
                return cardController.draw_card_female()
            else:
                raise ValueError()
        except ValueError:
            return Response('{"error": "ValueError", "message": "gender is invalid must be one of (m, f)"}', status=500, mimetype='application/json')
        except AssertionError:
            return Response('{"error": "AssertionError", "message": "gender is required"}', status=500, mimetype='application/json')

    def reset_graveyard():
        return cardController.reset_graveyard()

    def fetch_card_count():
        return cardController.fetch_card_count()