from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    # ==========================
    # 📡 Telegram API Credentials
    # ==========================

    API_ID = int(getenv("API_ID", 12345))  # Get this from https://my.telegram.org/apps
    API_HASH = getenv("API_HASH", "")      # Get this from https://my.telegram.org/apps
    TOKEN = getenv("TOKEN", "")            # Get this from @BotFather on Telegram

    OWNER_ID = int(getenv("OWNER_ID", 0))  # Your Telegram numeric user ID (Use @userinfobot to get it)
    OWNER_USERNAME = getenv("OWNER_USERNAME", "CertifiedCoder")  # Your Telegram username (without @)

    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "CertifiedCoders")     # Public support group username (without @)
    LOGGER_ID = int(getenv("LOGGER_ID", "-100"))                 # Telegram Channel/Group ID for logging events

    # ==========================
    # 🗄️ Database / Storage
    # ==========================

    MONGO_URI = getenv("MONGO_DB_URI", "")        # MongoDB URI (from your MongoDB provider, e.g., MongoDB Atlas)
    DB_NAME = getenv("DB_NAME", "AvaRobot")       # MongoDB database name (default is AvaRobot)

    # PostgreSQL URI (used for SQL-based modules like backups, stats, etc.)
    # Heroku and Railway provide this automatically as DATABASE_URL.
    # If you're deploying on a VPS, you can follow the guide here:
    # 👉 https://github.com/CertifiedCoders/AvaRobot/blob/Master/.github/docs/DatabaseSetup.md
    DATABASE_URL = getenv("DATABASE_URL", "")


    # Fix for Heroku-style DATABASE_URL (postgres:// → postgresql://)
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

    # ==========================
    # 🌐 External APIs (Optional)
    # ==========================

    DEEP_API = getenv("DEEP_API", "")             # Get from https://deepai.org/
    ARQ_API_KEY = getenv("ARQ_API_KEY", "")       # Get from https://t.me/ARQRobot
    SPAMWATCH_API = getenv("SPAMWATCH_API", "")   # Get from https://t.me/SpamWatchBot


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
