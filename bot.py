from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot configuration - USING YOUR PROVIDED TOKEN
TOKEN = "8133637370:AAFLj69-cRhx3D_ZFhzGd3gxjBUfb_sUab4"
CHANNEL_USERNAME = "@CryptoAirdropZone"  # Replace with your channel
GROUP_USERNAME = "@CryptoAirdropChat"    # Replace with your group
TWITTER_URL = "https://twitter.com/YourCryptoPage"  # Replace with your Twitter

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    welcome_message = (
        f"👋 Hey {user.first_name}!\n\n"
        "🎉 Welcome to the Exclusive Solana Airdrop!\n\n"
        "📋 To participate:\n"
        f"1. Join our channel: {CHANNEL_USERNAME}\n"
        f"2. Join our group: {GROUP_USERNAME}\n"
        f"3. Follow us on Twitter: {TWITTER_URL}\n\n"
        "💰 After joining, send your Solana wallet address below:"
    )
    
    # Create join buttons
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("👥 Join Group", url=f"https://t.me/{GROUP_USERNAME[1:]}")],
        [InlineKeyboardButton("🐦 Follow Twitter", url=TWITTER_URL)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(welcome_message, reply_markup=reply_markup)

def handle_wallet(update: Update, context: CallbackContext) -> None:
    wallet_address = update.message.text.strip()
    # No validation - accept any text as wallet
    confirmation = (
        "🎉 Congratulations! You've completed all steps!\n\n"
        "✅ 10 SOL is on its way to your wallet!\n"
        f"📬 Wallet address: `{wallet_address}`\n\n"
        "⏱ Estimated arrival: 2-5 minutes\n\n"
        "⚠️ Note: This is a test bot. No actual SOL will be sent."
    )
    
    update.message.reply_text(confirmation, parse_mode='Markdown')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_wallet))

    # Start bot
    logger.info("Starting bot...")
    updater.start_polling()
    logger.info("Bot is now running. Press Ctrl+C to stop.")
    updater.idle()

if __name__ == '__main__':
    main()
