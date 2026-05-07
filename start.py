from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import app

@app.on_message(filters.command("start"))
async def start(_, message):

    text = """
Hello 👋

I am a Professional Auto Rename Bot.

Commands:

/format - Set rename format
/viewformat - View format
/delformat - Delete format
/setthumb - Set thumbnail
/delthumb - Delete thumbnail
"""

    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Updates",
                    url="https://t.me"
                )
            ]
        ]
    )

    await message.reply_text(
        text,
        reply_markup=btn
    )