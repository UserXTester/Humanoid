# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}botecho text (optional -\n[button_text_1](https://t.me/TheHumanoid)\n[button_text_2](https://t.me/TeamHumanoid))`
   Send a message from your assistant bot.
"""

import re

from . import *

regex = r"\[(.*)\]\((\S*)\)"


def generate_url_button(text):
    btns = []
    if not text:
        return None
    bt_txt = re.sub(regex, "", text) or None
    matches = re.finditer(regex, text, re.MULTILINE)
    if not matches:
        return None
    for i, match in enumerate(matches):
        if match.group(2).endswith(":same"):
            btnurl = match.group(2)[:-5]
            if i == 0:
                btns.append([Button.url(text=match.group(1), url=btnurl)])
            else:
                btns[-1].append(Button.url(text=match.group(1), url=btnurl))
        else:
            btns.append([Button.url(text=match.group(1), url=match.group(2))])
    if not btns:
        btns = None
    return bt_txt, btns


@Humanoid_cmd(pattern="botecho")
async def button_parser(event):
    try:
        text = event.text.split(" ", 1)[1]
    except IndexError:
        return await eor(
            event,
            f"**Please give some text!**\n**Format:** `{hndlr}botecho text \n[button_text_1](https://t.me/TheHumanoid)\n[button_text_2](https://t.me/TeamHumanoid)`",
        )
    text, buttons = generate_url_button(text)
    try:
        if text is None:
            return await eor(event, "`Please provide a text too!`")
        await asst.send_message(event.chat_id, text, buttons=buttons)
        await eor(event, "Done. Message sent.")
    except Exception as e:
        await eod(event, "**ERROR:**\n{}".format(str(e)), time=5)
