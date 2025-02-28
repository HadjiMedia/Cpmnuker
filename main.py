from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7940607002:AAHPVMx_AsdyeIxPl_v_iOgN6-tGzOR8Dak"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your bot.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()