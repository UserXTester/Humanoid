# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}addsudo`
    Add Sudo Users by replying to user or using <space> separated userid(s)

• `{i}delsudo`
    Remove Sudo Users by replying to user or using <space> separated userid(s)

• `{i}listsudo`
    List all sudo users.
"""
from pyHumanoid.misc import sudoers

from . import *


@Humanoid_cmd(
    pattern="addsudo ?(.*)",
)
async def _(Human):
    if not Human.out and not is_fullsudo(Human.sender_id):
        return await eod(Human, "`This Command is Sudo Restricted!..`")
    inputs = Human.pattern_match.group(1)
    if str(Human.sender_id) in sudoers():
        return await eod(Human, "`Sudo users can't add new sudos!`", time=10)
    ok = await eor(Human, "`Updating SUDO Users List ...`")
    mmm = ""
    if Human.reply_to_msg_id:
        replied_to = await Human.get_reply_message()
        sender = replied_to.sender
        id = sender.id
        name = sender.first_name
    elif inputs:
        id = await get_user_id(inputs)
        try:
            name = (await Human.client.get_entity(int(id))).first_name
        except BaseException:
            name = ""
    else:
        return await eod(Human, "`Reply to a msg or add it's id/username.`")

    if id == Humanoid_bot.me.id:
        mmm += "You cant add yourself as Sudo User..."
    elif is_sudo(id):
        if name != "":
            mmm += f"[{name}](tg://user?id={id}) `is already a SUDO User ...`"
        else:
            mmm += f"`{id} is already a SUDO User...`"
    elif add_sudo(id):
        HumandB.set("SUDO", "True")
        if name != "":
            mmm += f"**Added [{name}](tg://user?id={id}) as SUDO User**"
        else:
            mmm += f"**Added **`{id}`** as SUDO User**"
    else:
        mmm += "`SEEMS LIKE THIS FUNCTION CHOOSE TO BREAK ITSELF`"
    await eod(ok, mmm)


@Humanoid_cmd(
    pattern="delsudo ?(.*)",
)
async def _(Human):
    if not Human.out and not is_fullsudo(Human.sender_id):
        return await eod(Human, "`This Command is Sudo Restricted!..`")
    inputs = Human.pattern_match.group(1)
    if str(Human.sender_id) in sudoers():
        return await eod(
            Human,
            "You are sudo user, You cant remove other sudo user.",
        )
    ok = await eor(Human, "`Updating SUDO Users List ...`")
    mmm = ""
    if Human.reply_to_msg_id:
        replied_to = await Human.get_reply_message()
        id = replied_to.sender_id
        name = replied_to.sender.first_name
    elif inputs:
        id = await get_user_id(inputs)
        try:
            name = (await Human.client.get_entity(int(id))).first_name
        except BaseException:
            name = ""
    else:
        return await eod(Human, "`Reply to a msg or add it's id/username.`")
    if not is_sudo(id):
        if name != "":
            mmm += f"[{name}](tg://user?id={id}) `wasn't a SUDO User ...`"
        else:
            mmm += f"`{id} wasn't a SUDO User...`"
    elif del_sudo(id):
        if name != "":
            mmm += f"**Removed [{name}](tg://user?id={id}) from SUDO User(s)**"
        else:
            mmm += f"**Removed **`{id}`** from SUDO User(s)**"
    else:
        mmm += "`SEEMS LIKE THIS FUNCTION CHOOSE TO BREAK ITSELF`"
    await eod(ok, mmm)


@Humanoid_cmd(
    pattern="listsudo$",
)
async def _(Human):
    ok = await eor(Human, "`...`")
    sudos = Redis("SUDOS")
    if sudos == "" or sudos is None:
        return await eod(Human, "`No SUDO User was assigned ...`", time=5)
    sumos = sudos.split(" ")
    msg = ""
    for i in sumos:
        try:
            name = (await Human.client.get_entity(int(i))).first_name
        except BaseException:
            name = ""
        if name != "":
            msg += f"• [{name}](tg://user?id={i}) ( `{i}` )\n"
        else:
            msg += f"• `{i}` -> Invalid User\n"
    m = HumandB.get("SUDO") if HumandB.get("SUDO") else "False"
    if m == "False":
        m = "[False](https://telegra.ph/Humanoid-04-06)"
    return await ok.edit(
        f"**SUDO MODE : {m}\n\nList of SUDO Users :**\n{msg}", link_preview=False
    )
