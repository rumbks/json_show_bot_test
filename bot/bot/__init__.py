from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

from credentials import BOT_TOKEN, APP_URL
from .handlers import start
from ..models import User


def setup_dispatcher() -> Dispatcher:
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher(bot=bot, update_queue=None)

    dispatcher.add_handler(CommandHandler("start", start))

    bot.setWebhook(APP_URL + "/bot/")
    return dispatcher


def is_start_command(update: Update) -> bool:
    try:
        return update.effective_message.entities[0]['type'] == 'bot_command'
    except (AttributeError, IndexError, KeyError):
        return False


dispatcher = setup_dispatcher()
