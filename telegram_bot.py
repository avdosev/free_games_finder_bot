from game_info import GameData
from dataclasses import asdict
import telepot

message = "Игрулька {name} доступна бесплатно [тут]({link})"


class TelegramBot:
    def __init__(self, api_key, chat_id):
        self.bt = telepot.Bot(api_key)
        self.chat_id = chat_id
        print(f"bot inited with: api_key={api_key}; chat_id={chat_id};")

    def notify(self, game: GameData):
        print("send response telegram")
        mes = message.format(**asdict(game))
        print("Message:", mes)
        self.bt.sendPhoto(self.chat_id, game.image_url, caption=mes)
