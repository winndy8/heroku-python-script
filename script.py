import subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def add_subtitles(mkv_file, subtitle_file):
    # Use FFmpeg to add subtitles to the MKV file permanently
    cmd = f"ffmpeg -i {mkv_file} -vf subtitles={subtitle_file} -c:a copy output.mkv"
    subprocess.run(cmd, shell=True)

def handle_message(update, context):
    # Retrieve the MKV file and subtitle file from the user's message
    mkv_file = update.message.document.file_id
    subtitle_file = update.message.document.file_id
    
    # Call the add_subtitles function to add subtitles to the MKV file
    add_subtitles(mkv_file, subtitle_file)

def handle_command(update, context):
    # Trigger the handle_message function when the user sends the /addsub command
    if update.message.text == '/addsub':
        handle_message(update, context)

# Set up the Telegram bot and add the command and message handlers
updater = Updater('6035735532:AAG-zSUZr2gzF9ZbWlfxSwhor8lxQfISuI0', use_context=True)
updater.dispatcher.add_handler(CommandHandler('addsub', handle_command))
updater.dispatcher.add_handler(MessageHandler(Filters.document, handle_message))

# Start the bot and keep it running
updater.start_polling()
updater.idle()
