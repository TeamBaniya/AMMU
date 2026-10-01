from AMMU.core.bot import RAJ
from AMMU.core.dir import dirr
from AMMU.core.git import git
from AMMU.core.userbot import Userbot
from AMMU.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RAJ()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
