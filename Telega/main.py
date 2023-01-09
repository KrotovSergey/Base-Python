# Hwork_GB_Tgbot_Krotov

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from log import log

def hello(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5806732798:AAHtEtKg56LYkCXfUmBj9BB-AaE2WpeA6h0')

updater.dispatcher.add_handler(CommandHandler("hello", hello))




print("bot started")

updater.start_polling()
updater.idle()