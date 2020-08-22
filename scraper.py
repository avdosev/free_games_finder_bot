import requests
import datetime
from pprint import pprint
from game_info import GameData, GameInformer


class EpicGamesStore(GameInformer):
    def __init__(self):
        res = requests.get(
            'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=ru&country=RU'
            '&allowCountries=RU'
        )
        self.page = res.json()

    def get_free_games(self):
        free_games = self.page['data']['Catalog']['searchStore']['elements']

        def is_active_game(game):
            promotions = game['promotions']
            return len(promotions['promotionalOffers']) != 0

        def to_dict(game):
            return GameData(
                game['keyImages'][0]['url'],
                game['title'],
                f"https://www.epicgames.com/store/ru/product/{game['productSlug']}"
            )

        free_games = [to_dict(game) for game in free_games if is_active_game(game)]
        return free_games
