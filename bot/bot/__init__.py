from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, InlineQueryHandler

from show_json_bot_test.settings import BOT_TOKEN, APP_URL
from .handlers import COMMAND_HANDLERS, INLINE_HANDLERS


def setup_dispatcher() -> Dispatcher:
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher(bot=bot, update_queue=None)

    for handler in COMMAND_HANDLERS:
        dispatcher.add_handler(CommandHandler(handler.__name__, handler))
    for handler in INLINE_HANDLERS:
        dispatcher.add_handler(InlineQueryHandler(handler))

    bot.setWebhook(f"{APP_URL}/bot/")
    return dispatcher


def is_start_command(update: Update) -> bool:
    try:
        return (
            update.effective_message.text == "/start"
            and update.effective_message.entities[0]["type"] == "bot_command"
        )
    except (AttributeError, IndexError, KeyError):
        return False


dispatcher = setup_dispatcher()

HANDLERS = [*COMMAND_HANDLERS]
