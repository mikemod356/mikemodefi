import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Configuration
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHANNEL_USERNAME = "@YourChannel"
GROUP_USERNAME = "@YourGroup"
TWITTER_URL = "https://twitter.com/YourTwitter"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("👥 Join Group", url=f"https://t.me/{GROUP_USERNAME[1:]}")],
        [InlineKeyboardButton("🐦 Follow Twitter", url=TWITTER_URL)],
    ]
    
    await update.message.reply_text(
        f"👋 Welcome {update.effective_user.first_name}!\n\n"
        "💰 Send your Solana wallet address to claim 10 SOL!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    wallet = update.message.text
    await update.message.reply_text(
        f"🎉 10 SOL will be sent to:\n\n`{wallet}`\n\n"
        "⚠️ Note: This is a test bot",
        parse_mode='Markdown'
    )

if __name__ == '__main__':
    if not TOKEN:
        logging.error("❌ Missing TELEGRAM_TOKEN!")
        exit(1)
        
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    logging.info("🤖 Bot started")
    application.run_polling()
