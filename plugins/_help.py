# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.

from pyHumanoid.dB.core import *
from telethon.errors.rpcerrorlist import BotInlineDisabledError as dis
from telethon.errors.rpcerrorlist import BotMethodInvalidError
from telethon.errors.rpcerrorlist import BotResponseTimeoutError as rep

from . import *


@Humanoid_cmd(pattern="help ?(.*)")
async def _help(Human):
    plug = Human.pattern_match.group(1)
    if plug:
        try:
            if plug in HELP:
                output = f"**Plugin** - `{plug}`\n"
                for i in HELP[plug]:
                    output += i
                output += "\n© @TeamHumanoid"
                await eor(Human, output)
            elif plug in CMD_HELP:
                kk = f"Plugin Name-{plug}\n\n✘ Commands Available -\n\n"
                kk += str(CMD_HELP[plug])
                await eor(Human, kk)
            else:
                try:
                    x = f"Plugin Name-{plug}\n\n✘ Commands Available -\n\n"
                    for d in LIST[plug]:
                        x += HNDLR + d
                        x += "\n"
                    x += "\n© @TeamHumanoid"
                    await eor(Human, x)
                except BaseException:
                    await eod(Human, get_string("help_1").format(plug), time=5)
        except BaseException:
            await eor(Human, "Error 🤔 occured.")
    else:
        tgbot = asst.me.username
        try:
            result = await Human.client.inline_query(tgbot, "Humand")
        except BotMethodInvalidError:
            z = []
            for x in LIST.values():
                for y in x:
                    z.append(y)
            cmd = len(z) + 10
            return await Human.client.send_message(
                Human.chat_id,
                get_string("inline_4").format(
                    OWNER_NAME,
                    len(PLUGINS) - 5,
                    len(ADDONS),
                    cmd,
                ),
                buttons=[
                    [
                        Button.inline("• Pʟᴜɢɪɴs", data="hrrrr"),
                        Button.inline("• Aᴅᴅᴏɴs", data="frrr"),
                    ],
                    [
                        Button.inline("Oᴡɴᴇʀ•ᴛᴏᴏʟꜱ", data="ownr"),
                        Button.inline("Iɴʟɪɴᴇ•Pʟᴜɢɪɴs", data="inlone"),
                    ],
                    [
                        Button.url(
                            "⚙️Sᴇᴛᴛɪɴɢs⚙️", url=f"https://t.me/{tgbot}?start=set"
                        ),
                    ],
                    [Button.inline("••Cʟᴏꜱᴇ••", data="close")],
                ],
            )
        except rep:
            return await eor(
                Human,
                get_string("help_2").format(HNDLR),
            )
        except dis:
            return await eor(Human, get_string("help_3"))
        await result[0].click(Human.chat_id, reply_to=Human.reply_to_msg_id, hide_via=True)
        await Human.delete()
