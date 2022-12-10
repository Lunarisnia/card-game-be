from src.routes.CardRouter import CardRouter

routes = [
    # /card
    CardRouter('/card/draw', 'Draw Card', CardRouter.draw_card),
    CardRouter('/card/resetGraveyard', 'Reset Graveyard', CardRouter.reset_graveyard, methods=['POST']),
    CardRouter('/card/count', 'Count Cards', CardRouter.fetch_card_count),
]