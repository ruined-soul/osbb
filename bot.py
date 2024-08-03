from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TOKEN
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(CommandHandler("help", help_handler))
    # Add more handlers as needed

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
