import requests
import youtube_dl
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "5642193"
API_HASH = "c28fc9ac88530587236175da89184d75"
BOT_TOKEN = "5208962076:AAFRivp9NqIABXvc0m8FI7PFxtaViYQeyeM"

def download_song(song_url):
  """Downloads a song from YouTube and saves it to the current directory."""
  response = requests.get(song_url)
  song_info = youtube_dl.extract_info(response.content, download=False)
  song_filename = f"{song_info['track']}.mp3"
  with open(song_filename, "wb") as f:
    f.write(response.content)

def main():
  song_url = input("Enter the URL of the song you want to download: ")
  download_song(song_url)

if __name__ == "__main__":
  main()
