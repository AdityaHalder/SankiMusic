from pyrogram import filters
from pyrogram.types import Message

from SankiMusic.utilities.strings import get_command
from SankiMusic import bot
from SankiMusic.misc import SUDOERS
from SankiMusic.modules.main.database.memorydatabase import (
    get_active_chats, get_active_video_chats)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@bot.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ʟɪsᴛ..."
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await bot.get_chat(x)).title
        except Exception:
            title = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        if (await bot.get_chat(x)).username:
            user = (await bot.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄʙᴏᴛ...")
    else:
        await mystic.edit_text(
            f"**ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄ ʙᴏᴛ :-**\n\n{text}",
            disable_web_page_preview=True,
        )


@bot.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs ʟɪsᴛ..."
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await bot.get_chat(x)).title
        except Exception:
            title = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        if (await bot.get_chat(x)).username:
            user = (await bot.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄ ʙᴏᴛ...")
    else:
        await mystic.edit_text(
            f"**ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs ᴏɴ ᴍᴜsɪᴄ ʙᴏᴛ :-**\n\n{text}",
            disable_web_page_preview=True,
        )
