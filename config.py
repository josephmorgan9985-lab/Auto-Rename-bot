import os

class Config:

    API_ID = int(os.environ.get("API_ID", "12345"))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    MONGO_URI = os.environ.get("MONGO_URI", "")

    FORCE_SUB = os.environ.get("FORCE_SUB", "")

    ADMIN = int(os.environ.get("ADMIN", "123456789"))