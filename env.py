import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "https://telegra.ph/file/00eaed55184edf059dbf7.jpg")
MONGO_URL = os.getenv("mongodb+srv://SachinSanatani:SACHINxSANATANI@sanatani.bnmsfbd.mongodb.net/?retryWrites=true&w=majority&appName=Sanatani")
LOG_GROUP_ID = os.getenv("-1002090474484")

if not API_ID:
    raise SystemExit("ɴᴏ ᴀᴘɪ_ɪᴅ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")
elif not API_HASH:
    raise SystemExit("ɴᴏ ᴀᴘɪ_ʜᴀꜱʜ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")
elif not BOT_TOKEN:
    raise SystemExit("ɴᴏ ʙᴏᴛ_ᴛᴏᴋᴇɴ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("ᴀᴘɪ_ɪᴅ ɪꜱ ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ɪɴᴛᴇɢᴇʀ. ᴇxɪᴛɪɴɢ...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
