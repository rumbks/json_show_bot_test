from telegram import (
    Update,
    InlineQueryResult,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from telegram.ext import CallbackContext

from bot.models import User


def start(update: Update, context):
    GREETING = """🔸 @RumbksShowJsonBot v2020.11 - Bot returns json for all sent messages.

Messages editing and inline queries are also supported.

Enjoy! ☺️"""
    user_dict = update.effective_user.to_dict()
    User.objects.update_or_create(
        id=user_dict["id"],
        defaults={
            key: value
            for key, value in user_dict.items()
            if key
            in [field.name for field in User._meta.get_fields() if field.name != "id"]
        },
    )

    update.message.reply_text(GREETING)


def inline(update: Update, context: CallbackContext):
    results = [
        InlineQueryResultArticle(
            id="id", title=" f", input_message_content=InputTextMessageContent(" f")
        )
    ]
    update.inline_query.answer(  # I have found a bug in python_telegram_bot API. answer method raises and exception when there's no results
        results, switch_pm_text="Your json was sent to pm", switch_pm_parameter="start"
    )

COMMAND_HANDLERS = [start]
INLINE_HANDLERS = [inline]
