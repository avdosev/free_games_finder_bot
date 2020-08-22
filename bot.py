from telegram_bot import TelegramBot
from scraper import EpicGamesStore
from config import *
from typing import List
from game_info import GameInformer, GameData
from storage import Notified


if __name__ == '__main__':
    notified_games = Notified()
    informers: List[GameInformer] = [
        EpicGamesStore()
    ]
    tb = TelegramBot(TELEGRAM_API_KEY, TELEGRAM_CHAT_ID)
    free_games: List[GameData] = []
    for informer in informers:
        free_games.extend(informer.get_free_games())
    for free_game in free_games:
        if not notified_games.has(free_game):
            print('Free not notified game: ', free_game)
            tb.notify(free_game)
            notified_games.add(free_game)
