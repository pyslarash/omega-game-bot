import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Load environment variables from .env file
load_dotenv()

# Get the Telegram Bot token from .env file
TELEGRAM_BOT_TOKEN = os.getenv("ENV_TELEGRAM_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Buttons
enter_the_world = InlineKeyboardButton(text="Enter the World! ", callback_data="In_First_button")

# STARTING THE GAME
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Hello, welcome to the game OMEGA! Type /rules to read the instructions.")

# LIST GAME RULES
async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Welcome to the OMEGA, my friends. Here are some rules of the game... To start the game, use /start_game")

# INTRO TO THE WORLD
async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Photo caption
    caption = "In a realm where the past meets the future, welcome to the Omega, a world where the charm of steampunk entwines with the relentless advance of cybernetic technology. Here, towering brass and iron structures coexist harmoniously with sleek digital computers, creating a vibrant symphony of innovation. You, a daring adventurer, have been chosen to shape the Empire's fate. Legends speak of powerful ancient artifacts scattered across the land, each capable of either bolstering the regime's dominion or leading to its downfall. Embark on a quest of wonder, mystery, and danger, where your decisions will shape the destiny of this unique steampunk-cyberpunk universe, unraveling the enigma as your adventure begins."
    
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                   photo="./img/cityscape.png", 
                                   caption=caption)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    rules_handler = CommandHandler('rules', rules)
    start_game_handler = CommandHandler('start_game', start_game)
    
    application.add_handler(start_handler)
    application.add_handler(rules_handler)
    application.add_handler(start_game_handler)
    
    application.run_polling()