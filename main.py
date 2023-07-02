import requests
import json

from telegram.bot import Bot
from telegram.ext import MessageHandler, Filters

# Create a bot using your Telegram bot token
bot = Bot(token='5208962076:AAFRivp9NqIABXvc0m8FI7PFxtaViYQeyeM')

# Create a message handler for song requests
def song_request(update, context):
    # Get the song name from the user
    song_name = update.message.text

    # Use the requests library to download the song from YouTube
    response = requests.get(f'https://www.youtube.com/results?search_query={song_name}')
    song_url = response.json()['items'][0]['url']

    # Save the song to a file
    song_file = requests.get(song_url)
    with open(f'{song_name}.mp3', 'wb') as f:
        f.write(song_file.content)

    # Send the song file to the user
    bot.send_document(update.message.chat_id, f'{song_name}.mp3')

# Register the message handler
updater = Updater(bot=bot, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, song_request))

# Start the bot
updater.start_polling()
updater.idle()
