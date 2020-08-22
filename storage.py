import json
from game_info import GameData


class Notified:
    def __init__(self):
        self.path = 'notified_games.txt'

    def add(self, game: GameData):
        with open(self.path, 'a') as file:
            print(game.name, file=file)

    def has(self, game: GameData):
        try:
            with open(self.path, 'r') as file:
                for game_name in file:
                    game_name = game_name[:-1]
                    if game_name == game.name:
                        return True
        except FileNotFoundError:
            pass
        return False
