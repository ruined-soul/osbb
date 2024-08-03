# handlers/status_handler.py
from telegram import Update
from telegram.ext import CallbackContext
from utils.helpers import fetch_status

def status_handler(update: Update, context: CallbackContext):
    """
    Handle the /status command and respond with the bot's status.
    """
    status_message = fetch_status()
    update.message.reply_text(status_message)
