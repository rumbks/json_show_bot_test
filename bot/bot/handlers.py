
def start(update, context):
    GREETING = """🔸 @RumbksShowJsonBot v2020.11 - Bot returns json for all sent messages.

Messages editing and inline queries are also supported.

Enjoy! ☺️"""

    update.message.reply_text(GREETING)
