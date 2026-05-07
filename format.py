from pyrogram import filters
from bot import app
from database.users import set_format, get_format

@app.on_message(filters.command("format"))
async def format_cmd(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/format {filename}"
        )

    fmt = message.text.split(" ", 1)[1]

    await set_format(message.from_user.id, fmt)

    await message.reply_text("✅ Format Saved")

@app.on_message(filters.command("viewformat"))
async def view_format(_, message):

    fmt = await get_format(message.from_user.id)

    if not fmt:
        return await message.reply_text("No format saved")

    await message.reply_text(f"Your Format:\n\n{fmt}")

@app.on_message(filters.command("delformat"))
async def del_format(_, message):

    await set_format(message.from_user.id, None)

    await message.reply_text("🗑 Format Deleted")