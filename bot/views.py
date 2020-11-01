import json
from collections import OrderedDict

from django.http import HttpRequest, JsonResponse
import telegram
from telegram.parsemode import ParseMode

from bot.bot import dispatcher, is_start_command


def telegram_request_handler(request: HttpRequest):
    def prettify_json(json_: OrderedDict):
        return f"```\n{json.dumps(body, ensure_ascii=False, indent=1)}```"
    body = json.loads(request.body, object_pairs_hook=OrderedDict)
    update = telegram.Update.de_json(body, dispatcher.bot)
    if is_start_command(update):
        dispatcher.process_update(update)
    else:
        update.effective_user.send_message(text=prettify_json(body), parse_mode=ParseMode.MARKDOWN)
    return JsonResponse({})
