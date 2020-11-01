from telegram import Update

from bot.models import User


def start(update: Update, context):
    GREETING = """🔸 @RumbksShowJsonBot v2020.11 - Bot returns json for all sent messages.

Messages editing and inline queries are also supported.

Enjoy! ☺️"""
    user = User(
        **{
            key: value
            for key, value in update.effective_user.to_dict().items()
            if key in [field.name for field in User._meta.get_fields()]
        }
    )
    user.save()

    update.message.reply_text(GREETING)
