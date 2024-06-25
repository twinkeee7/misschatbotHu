from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "6718764653"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "@Riseeuniversee")
UPDATE_CHNL = getenv("UPDATE_CHNL", "@Riseeuniversee")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@SupremeXlevel")

# Random Start Images
IMG = [
    "https://graph.org/file/b94fa0a71c5e9f8b53382.jpg",
    "https://graph.org/file/b2146698ae7b91efab281.jpg",
    "https://graph.org/file/ae47ae84e134bfaaf56d8.jpg",
    "https://graph.org/file/39dc33af8d49a555824af.jpg",
    "https://graph.org/file/ca07e2c89c1158637ed39.jpg",
]


# Random Stickers
STICKER = [
    "https://t.me/addstickers/a_6718764653_by_Toga_Robot"
    ,
]


EMOJIOS = [
    "🙈",
    "💗",
    "💭",
]
