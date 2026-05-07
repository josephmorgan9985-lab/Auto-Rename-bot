import os
from pyrogram import filters
from bot import app
from database.users import get_format, get_thumbnail

@app.on_message(filters.document)
async def rename_file(_, message):

    user_id = message.from_user.id

    fmt = await get_format(user_id)

    if not fmt:
        return await message.reply_text(
            "Set format first using /format"
        )

    old_name = message.document.file_name

    if "." in old_name:
        ext = old_name.split(".")[-1]
    else:
        ext = "mkv"

    filename = old_name.rsplit(".", 1)[0]

    new_name = fmt.replace(
        "{filename}",
        filename
    )

    new_name = f"{new_name}.{ext}"

    msg = await message.reply_text(
        "📥 Downloading File..."
    )

    path = await message.download()

    os.rename(path, new_name)

    thumb = await get_thumbnail(user_id)

    await msg.edit("📤 Uploading File...")

    await message.reply_document(
        document=new_name,
        thumb=thumb,
        caption=f"✅ {new_name}"
    )

    os.remove(new_name)

    await msg.delete()