# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.

import asyncio
import time
from pyHumanoid import *
from pyHumanoid.dB import *
from pyHumanoid.functions.all import *
from pyHumanoid.functions.sudos import *
from pyHumanoid.version import Humanoid_version
from telethon import Button
from telethon.tl import functions, types
try:
    from strings import get_string
except ModuleNotFoundError:
    os.system("pip install -U strings")
    os.system("pip install -U pystrings")
    from strings import get_string

os.system("pip install lxml")
os.system("pip install hachoir")
os.system("pip install shazamio")
os.system("pip install selenium qrcode ProfanityDetector apscheduler gingerit jikanpy")
try:
    import glitch_me
except ModuleNotFoundError:
    os.system(
        "git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me"
    )


start_time = time.time()

OWNER_NAME = Humanoid_bot.me.first_name
OWNER_ID = Humanoid_bot.me.id

List = []
Dict = {}
N = 0

NOSPAM_CHAT = [
    -1001387666944,  # @PyrogramChat
    -1001109500936,  # @TelethonChat
    -1001050982793,  # @Python
    -1001256902287,  # @DurovsChat
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]
