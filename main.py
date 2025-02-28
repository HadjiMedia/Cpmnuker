import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7940607002:AAHPVMx_AsdyeIxPl_v_iOgN6-tGzOR8Dak"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm your bot.")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(main())  # Use this instead of asyncio.run()