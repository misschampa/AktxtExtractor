
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

app = Client("AktxtExtractor", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start_message(client, message):
    message.reply("Hello! Welcome to AktxtExtractor bot.")

if __name__ == "__main__":
    app.run()
```
