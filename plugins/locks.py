# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}lock <msgs/media/sticker/gif/games/inline/polls/invites/pin/changeinfo>`
    Lock the Used Setting in Used Group.

• `{i}unlock <msgs/media/sticker/gif/games/inline/polls/invites/pin/changeinfo>`
    UNLOCK the Used Setting in Used Group.

"""
from pyHumanoid.functions.all import lucks, unlucks
from telethon.tl.functions.messages import EditChatDefaHumanBannedRightsRequest

from . import *


@Humanoid_cmd(
    pattern="lock ?(.*)",
    groups_only=True,
    admins_only=True,
    type=["official", "manager"],
    ignore_dualmode=True,
)
async def lockho(e):
    mat = e.pattern_match.group(1)
    if not mat:
        return await eod(e, "`Give some Proper Input..`")
    try:
        ml = lucks(mat)
    except BaseException:
        return await eod(e, "`Incorrect Input`")
    await e.client(EditChatDefaHumanBannedRightsRequest(e.chat_id, ml))
    await eor(e, f"Locked - `{mat}` ! ")


@Humanoid_cmd(
    pattern="unlock ?(.*)",
    groups_only=True,
    admins_only=True,
    type=["official", "manager"],
    ignore_dualmode=True,
)
async def unlckho(e):
    mat = e.pattern_match.group(1)
    if not mat:
        return await eod(e, "`Give some Proper Input..`")
    try:
        ml = unlucks(mat)
    except BaseException:
        return await eod(e, "`Incorrect Input`")
    await e.client(EditChatDefaHumanBannedRightsRequest(e.chat_id, ml))
    await eor(e, f"Unlocked - `{mat}` ! ")
