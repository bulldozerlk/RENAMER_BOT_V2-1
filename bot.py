from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5584644386:AAEXiEOU3e1tiHWYq8OOKW9mU2g_iMQKjMY")
ADMIN = "5363862546"
API_ID = int(os.environ.get("API_ID", "18497514"))
DB_URL = "mongodb+srv://990909jjjjfdrew4rfrfdrdsese4567890moko:990909jjjjfdrew4rfrfdrdsese4567890moko@cluster0.lkqip.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "fk"
API_HASH = os.environ.get("API_HASH", "d09d122ec6dce14a421e177b88bc1293")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
