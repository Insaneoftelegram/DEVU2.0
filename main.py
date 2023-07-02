import requests
import youtube_dl

def download_song(song_url):
  """Downloads a song from YouTube and saves it to the current directory."""
  response = requests.get(song_url)
  song_info = youtube_dl.extract_info(response.content, download=False)
  song_filename = f"{song_info['title']}.mp3"

  # Check if the song already exists
  if os.path.exists(song_filename):
    print(f"The song '{song_filename}' already exists.")
    return

  with open(song_filename, "wb") as f:
    f.write(response.content)

  print(f"Successfully downloaded the song '{song_filename}'.")

def handle_message(update, context):
  """Handles a message from a user."""
  message = update.message.text

  if message.startswith("/download"):
    song_url = message.split(" ")[1]
    download_song(song_url)

def main():
  """Starts the bot."""
  bot = TelegramBot(token="5208962076:AAFRivp9NqIABXvc0m8FI7PFxtaViYQeyeM")
  bot.register_handler(handle_message)
  bot.run()

if __name__ == "__main__":
  main()
