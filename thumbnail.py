from pyrogram import filters
from bot import app
from database.users import set_thumbnail

@app.on_message(filters.command("setthumb"))
async def set_thumb(_, message):

    await message.reply_text(
        "Send a photo to save thumbnail"
    )

@app.on_message(filters.photo)
async def save_thumb(_, message):

    file_id = message.photo.file_id

    await set_thumbnail(
        message.from_user.id,
        file_id
    )

    await message.reply_text(
        "✅ Thumbnail Saved"
    )