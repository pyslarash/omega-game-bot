import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Telegram Bot token from .env file
TELEGRAM_BOT_TOKEN = os.getenv("ENV_TELEGRAM_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Hello, welcome to the game OMEGA! Type /rules to read the instructions.")
    
async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Welcome to the OMEGA, my friends. Here are some rules of the game...")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    rules_handler = CommandHandler('rules', rules)
    
    application.add_handler(start_handler)
    application.add_handler(rules_handler)
    
    application.run_polling()