# SudoR2spr WOODcraft
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID")
API_HASH  = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SESSION = os.environ.get("SESSION")
FORCESUB = os.environ.get("FORCESUB")
AUTH = os.environ.get("AUTH")

# Raise an error if any critical environment variable is missing
# if not API_ID or not API_HASH or not BOT_TOKEN:
#     raise ValueError("API_ID, API_HASH, and BOT_TOKEN must be set as environment variables")
