from io import BytesIO
from time import sleep
from typing import Optional, List
from telegram import TelegramError, Chat, Message
from telegram import Update, Bot, User
from telegram import ParseMode
from telegram.error import BadRequest
from telegram.ext import MessageHandler, Filters, CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import escape_markdown
from GilbertAnimeBot.modules.helper_funcs.chat_status import is_user_ban_protected, user_admin

import random
import telegram
import GilbertAnimeBot.modules.sql.users_sql as sql
from GilbertAnimeBot import dispatcher, OWNER_ID, LOGGER
from GilbertAnimeBot.modules.helper_funcs.filters import CustomFilters
from GilbertAnimeBot.modules.disable import DisableAbleCommandHandler

MESSAGES = (
    "Happy birthday ",
    "Heppi burfdey ",
    "Hep burf ",
    "Happy day of birthing ",
    "Sadn't deathn't-day ",
    "Oof, you were born today ",
)

@user_admin
def birthday(update, context):
    args = context.args
    if args:
        username = str(",".join(args))
    context.bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    for i in range(5):
        bdaymessage = random.choice(MESSAGES)
        update.effective_message.reply_text(bdaymessage + username)

BIRTHDAY_HANDLER = DisableAbleCommandHandler("birthday", birthday, pass_args=True, filters=Filters.chat_type.groups, run_async=True)

dispatcher.add_handler(BIRTHDAY_HANDLER)
