# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.

from pyHumanoid import *
from pyHumanoid.dB.database import Var
from pyHumanoid.functions.all import *
from telethon import Button, custom

from strings import get_languages, get_string

OWNER_NAME = Humanoid_bot.me.first_name
OWNER_ID = Humanoid_bot.me.id


async def setit(event, name, value):
    try:
        HumandB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
