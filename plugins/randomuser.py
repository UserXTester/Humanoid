# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}randomuser`
   Generate details about a random user.
"""
from . import *


@Humanoid_cmd(pattern="randomuser")
async def _gen_data(event):
    x = await eor(event, get_string("com_1"))
    msg, pic = get_random_user_data()
    await event.reply(file=pic, message=msg)
    await x.delete()
