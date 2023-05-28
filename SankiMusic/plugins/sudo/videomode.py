from pyrogram import filters
from pyrogram.types import Message

from SankiMusic.utilities import config
from SankiMusic.utilities.strings import get_command
from SankiMusic import bot
from SankiMusic.misc import SUDOERS
from SankiMusic.modules.main.database import add_off, add_on
from SankiMusic.modules.main.decorators.language import language

# Commands
VIDEOMODE_COMMAND = get_command("VIDEOMODE_COMMAND")


@bot.on_message(filters.command(VIDEOMODE_COMMAND) & SUDOERS)
@language
async def videoloaymode(client, message: Message, _):
    usage = _["vidmode_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "download":
        await add_on(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_2"])
    elif state == "m3u8":
        await add_off(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_3"])
    else:
        await message.reply_text(usage)
