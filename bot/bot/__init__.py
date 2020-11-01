from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, InlineQueryHandler

from credentials import BOT_TOKEN, APP_URL
from .handlers import start, inline


def setup_dispatcher() -> Dispatcher:
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher(bot=bot, update_queue=None)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(InlineQueryHandler(inline))

    bot.setWebhook(f"{APP_URL}/bot/")
    return dispatcher


def is_start_command(update: Update) -> bool:
    try:
        return update.effective_message.entities[0]['type'] == 'bot_command'
    except (AttributeError, IndexError, KeyError):
        return False


dispatcher = setup_dispatcher()
