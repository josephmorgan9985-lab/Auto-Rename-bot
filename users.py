from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

mongo = AsyncIOMotorClient(Config.MONGO_URI)
db = mongo.renamebot
users = db.users

async def set_format(user_id, fmt):
    await users.update_one(
        {"_id": user_id},
        {"$set": {"format": fmt}},
        upsert=True
    )

async def get_format(user_id):
    user = await users.find_one({"_id": user_id})

    if user:
        return user.get("format")

    return None

async def set_thumbnail(user_id, file_id):
    await users.update_one(
        {"_id": user_id},
        {"$set": {"thumb": file_id}},
        upsert=True
    )

async def get_thumbnail(user_id):
    user = await users.find_one({"_id": user_id})

    if user:
        return user.get("thumb")

    return None