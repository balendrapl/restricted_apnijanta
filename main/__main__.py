
import logging
import time
import sys
from pyrogram import Client
from telethon.sync import TelegramClient

#from . import bot
#12

#logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
#                    level=logging.WARNING)

#Logger setup
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)
#logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Bot start time for tracking uptime
botStartTime = time.time()

#Telegram bot & userbot credentials 
API_ID = 25912801
API_HASH = "f14e8717578935103e2774559184a345"
BOT_TOKEN = "6728704718:AAHbgt-igQ0pfqderXjQtG2IdYNPQw-Wj7I"
SESSION = "BQGLZeEAkA1Nqo547S1_Bgeyk6evl0bFEpHN9H6OnGpcBNj-p0IyiaMcg-rFjgOb4wsx3uNZTpK7v7Kad0FLILPrYXegfILRY_Ec5ln5XVcCZu4ouZ9tt-rKXFXRqqe0U1_73GWHWBOnP4A4vKNgYPHlylErNYnJawrhLGE202G3lt0NuUPLxdpPP-DsV6wNgeIfpd4rGDP-MCAKzbbntOU3g7mnFi4CV6q-zbrQEfiAaKQmAE5cDVcdOqSy-YD2SBnI0Wuth5ZVJ3HozAPGWkWLZJGQcBqYSc4rwjJ3e5LgZwtax8MKFYn2uaqGQtNqU0ol-Kic3QRrbrveblzz7jtoVJMAAAAABN4sJoAA"

#Print statements to confirm successful deployment
print("Successfully deployed!")
print("By Mr. Invisible • Mr_Invisible_bots")

# Telethon bot setup
telethon_bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Pyrogram userbot setup
userbot = Client("myacc", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

# Start the userbot
try:
    userbot.start()
    print("Userbot started successfully!")
except BaseException:
    print("Userbot Error! Have you added SESSION while deploying?")
    sys.exit(1)

# Pyrogram bot setup
Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Start the Pyrogram bot
try:
    Bot.start()
    print("Pyrogram bot started successfully!")
except Exception as e:
    logging.info(e)
    sys.exit(1)

# Keep the bots running
try:
    telethon_bot.run_until_disconnected()  # For Telethon bot
    # Bot.idle()  # Uncomment this if you're using Pyrogram for the bot
except KeyboardInterrupt:
    print("Bot stopped manually!")


# if __name__ == "__main__":
#     from . import bot
#     import glob
#     from pathlib import Path
#     from main.utils import load_plugins
    
#     path = "main/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as a:
#             patt = Path(a.name)
#             plugin_name = patt.stem
#             load_plugins(plugin_name.replace(".py", ""))
    # logger.info("Bot Started :)")
    # bot.run_until_disconnected()
    
