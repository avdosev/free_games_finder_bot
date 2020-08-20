from telegram_bot import TelegramBot
from scraper import EpicGamesStore
from config import *

if __name__ == '__main__':
    tb = TelegramBot(TELEGRAM_API_KEY, TELEGRAM_CHAT_ID)
    tb.notify(EpicGamesStore().get_free_games()[0])
