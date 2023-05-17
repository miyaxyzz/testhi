import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from telegram.ext import Updater, CommandHandler
from telegram import ParseMode

# Path to the client secrets JSON file
CLIENT_SECRETS_FILE = 'client_secrets.json'

# Telegram bot token
BOT_TOKEN = '6103767186:AAEAi5sxhE3-insz6WfuOomq0rnYL9mbJ5M'

# Telegram group chat ID
GROUP_CHAT_ID = '-928770489'

# Monitor Google Drive for new files and folders
for file in drive.ListFile({'q': f"'{DRIVE_FOLDER_ID}' in parents and trashed=false"}).GetList():
    on_file_created(file)

for folder in drive.ListFile({'q': f"'{DRIVE_FOLDER_ID}' in parents and trashed=false and mimeType='application/vnd.google-apps.folder'"}).GetList():
    on_folder_created(folder)

# Initialize GoogleDrive instance
gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.txt")

if gauth.credentials is None:
    # Authenticate if no credentials found
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh credentials if expired
    gauth.Refresh()
else:
    # Authorize the credentials
    gauth.Authorize()

# Save the credentials
gauth.SaveCredentialsFile("credentials.txt")
drive = GoogleDrive(gauth)

# Function to send a Telegram message
def send_message(bot, chat_id, text):
    bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

# Handler for the /start command
def start(update, context):
    send_message(context.bot, update.message.chat_id, "Bot is running!")

# Handler for new file creation
def on_file_created(file):
    send_message(context.bot, GROUP_CHAT_ID, f"New file created: {file['title']}")

# Handler for new folder creation
def on_folder_created(folder):
    send_message(context.bot, GROUP_CHAT_ID, f"New folder created: {folder['title']}")

def main():
    # Create the Updater and pass your bot token
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the handlers
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Monitor Google Drive for new files and folders
    for file in drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList():
        on_file_created(file)

    for folder in drive.ListFile({'q': "'root' in parents and trashed=false and mimeType='application/vnd.google-apps.folder'"}).GetList():
        on_folder_created(folder)

    # Poll Google Drive every 5 seconds for new files and folders
    updater.job_queue.run_repeating(lambda context: monitor_drive(context.bot), interval=5, first=0)

    # Run the bot
    updater.idle()

if __name__ == '__main__':
    main()
