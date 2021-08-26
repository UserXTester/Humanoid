# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.

"""
✘ Commands Available -

•`{i}addclean`
    Clean all Upcoming action msg in added chat like someone joined/left/pin etc.

•`{i}remclean`
    Remove chat from database.

•`{i}listclean`
   To get list of all chats where its activated.

"""

from pyHumanoid.functions.clean_db import *

from . import *


@Humanoid_cmd(pattern="addclean$", admins_only=True)
async def _(e):
    add_clean(e.chat_id)
    await eod(e, "Added Clean Action Setting For this Chat")


@Humanoid_cmd(pattern="remclean$")
async def _(e):
    rem_clean(e.chat_id)
    await eod(e, "Removed Clean Action Setting For this Chat")


@Humanoid_cmd(pattern="listclean$")
async def _(e):
    k = HumandB.get("CLEANCHAT")
    if k:
        k = k.split(" ")
        o = ""
        for x in k:
            try:
                title = e.chat.title
            except BaseException:
                title = "`Invalid ID`"
            o += x + " " + title + "\n"
        await eor(e, o)
    else:
        await eod(e, "`No Chat Added`")
