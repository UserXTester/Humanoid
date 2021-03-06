# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.

"""
✘ Commands Available -

**DataBase Commands, do not use if you don't know what it is.**

• `{i}setredis key | value`
    Redis Set Value.
    e.g :
    `{i}setredis hi there`
    `{i}setredis hi there | Humanoid here`

• `{i}delredis key`
    Delete Key from Redis DB

• `{i}renredis old keyname | new keyname`
    Update Key Name
"""

import re

from . import *


@Humanoid_cmd(
    pattern="setredis ?(.*)",
)
async def _(Human):
    if not Human.out:
        if not is_fullsudo(Human.sender_id):
            return await eod(Human, "`This Command Is Sudo Restricted.`")
    ok = await eor(Human, "`...`")
    try:
        delim = " " if re.search("[|]", Human.pattern_match.group(1)) is None else " | "
        data = Human.pattern_match.group(1).split(delim, maxsplit=1)
        HumandB.set(data[0], data[1])
        redisdata = Redis(data[0])
        await ok.edit(
            "Redis Key Value Pair Updated\nKey : `{}`\nValue : `{}`".format(
                data[0],
                redisdata,
            ),
        )
    except BaseException:
        await ok.edit("`Something Went Wrong`")


@Humanoid_cmd(
    pattern="delredis ?(.*)",
)
async def _(Human):
    if not Human.out:
        if not is_fullsudo(Human.sender_id):
            return await eod(Human, "`This Command Is Sudo Restricted.`")
    ok = await eor(Human, "`Deleting data from Redis ...`")
    try:
        key = Human.pattern_match.group(1)
        k = HumandB.delete(key)
        if k == 0:
            return await ok.edit("`No Such Key.`")
        await ok.edit(f"`Successfully deleted key {key}`")
    except BaseException:
        await ok.edit("`Something Went Wrong`")


@Humanoid_cmd(
    pattern="renredis ?(.*)",
)
async def _(Human):
    if not Human.out:
        if not is_fullsudo(Human.sender_id):
            return await eod(Human, "`This Command Is Sudo Restricted.`")
    ok = await eor(Human, "`...`")
    delim = " " if re.search("[|]", Human.pattern_match.group(1)) is None else " | "
    data = Human.pattern_match.group(1).split(delim)
    if Redis(data[0]):
        try:
            HumandB.rename(data[0], data[1])
            await ok.edit(
                "Redis Key Rename Successful\nOld Key : `{}`\nNew Key : `{}`".format(
                    data[0],
                    data[1],
                ),
            )
        except BaseException:
            await ok.edit("Something went wrong ...")
    else:
        await ok.edit("Key not found")
