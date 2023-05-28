from pyrogram import filters
from pyrogram.types import Message

from SankiMusic.utilities.config import BANNED_USERS
from SankiMusic.utilities.strings import get_command
from SankiMusic import bot
from SankiMusic.modules.core.call import Kaal
from SankiMusic.utilities.events.filters import command
from SankiMusic.modules.main.database import is_music_playing, music_on
from SankiMusic.modules.main.decorators import AdminRightsCheck
from SankiMusic.utilities.inline.play import close_keyboard

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@bot.on_message(
    command(RESUME_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Kaal.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )
