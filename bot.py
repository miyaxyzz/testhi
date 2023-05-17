from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from telegram.ext import Updater, CommandHandler
from telegram import ParseMode
import pickle

# Load the credentials from token.pickle
with open('token.pickle', 'rb') as token_file:
    credentials = pickle.load(token_file)

# Create a Google Drive service using the credentials
drive_service = build('drive', 'v3', credentials=credentials)

# Telegram bot token
BOT_TOKEN = '6103767186:AAEAi5sxhE3-insz6WfuOomq0rnYL9mbJ5M'

# Telegram group chat ID
GROUP_CHAT_ID = '-928770489'

# Google Drive folder ID
DRIVE_FOLDER_ID = '15KQTULld-a7bPrvdKZRfissk0eDw6vQI'

# Function to send a Telegram message
def send_message(bot, chat_id, text):
    bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

# Handler for the /start command
def start(update, context):
    send_message(context.bot, update.message.chat_id, "Bot is running!")

# Handler for new file creation
def on_file_created(update, context):
    send_message(context.bot, GROUP_CHAT_ID, f"New file created: {update['name']}")

# Handler for new folder creation
def on_folder_created(update, context):
    send_message(context.bot, GROUP_CHAT_ID, f"New folder created: {update['name']}")

def main():
    # Create the Updater and pass your bot token
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the handlers
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    try:
        # Monitor Google Drive for new files and folders
        results = drive_service.files().list(q=f"'{DRIVE_FOLDER_ID}' in parents and trashed=false", pageSize=10).execute()
        items = results.get('files', [])
        for item in items:
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                on_folder_created(item, updater)
            else:
                on_file_created(item, updater)

        # Run the bot
        updater.idle()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
