from pyrogram import filters
from pyrogram.errors import UserNotParticipant
from bot import app
from config import Config

@app.on_message(filters.private)
async def force_sub(_, message):

    if not Config.FORCE_SUB:
        return

    try:
        await app.get_chat_member(
            Config.FORCE_SUB,
            message.from_user.id
        )

    except UserNotParticipant:
        return await message.reply_text(
            f"Join @{Config.FORCE_SUB} First"
        )