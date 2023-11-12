from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.utils.errors import capture_err
from VIPMUSIC.utils.pastebin import VIPBin as paste


@app.on_message(filters.command("paste"))
@capture_err
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰  𝙼𝙴𝚂𝚂𝙰𝙶𝙴  𝚆𝙸𝚃𝙷 /paste")
    m = await message.reply_text("𝐏𝙰𝚂𝚃𝙸𝙽𝙶...........")
    if message.reply_to_message.text:
        content = str(message.reply_to_message.text)
    elif message.reply_to_message.document:
        document = message.reply_to_message.document
        if document.file_size > 1048576:
            return await m.edit("You can only paste files smaller than 1MB.")
        if not pattern.search(document.mime_type):
            return await m.edit("Only text files can be pasted.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    preview = link + "/preview.png"
    button = InlineKeyboard(row_width=1)
    button.add(InlineKeyboardButton(text="Paste Link", url=link))

    if await isPreviewUp(preview):
        try:
            await message.reply_photo(photo=preview, quote=False, reply_markup=button)
            return await m.delete()
        except Exception:
            pass
    return await m.edit(link)
