from aiohttp import ClientSession
from .console import LOGGER

from SankiMusic.modules.core.app import App
from SankiMusic.modules.core.bot import Bot
from SankiMusic.modules.core.dirs import dirr
from SankiMusic.modules.core.git import git
from SankiMusic.misc import dbb, heroku, sudo

dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = App()

bot = Bot()


from SankiMusic.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
