from pyrogram import filters
from bot import app
from config import Config
from database.users import users

@app.on_message(filters.command("broadcast") & filters.user(Config.ADMIN))
async def broadcast(_, message):

    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a message"
        )

    total = 0

    async for user in users.find():
        try:
            await message.reply_to_message.copy(user['_id'])
            total += 1
        except:
            pass

    await message.reply_text(
        f"Broadcast Sent To {total} Users"
    )