# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available -

•`{i}calc` - Inline Calculator

"""
import re

from . import *


@Humanoid_cmd(pattern="calc")
async def icalc(e):
    HumandB.delete("calc")
    resHumans = await e.client.inline_query(asst.me.username, "calc")
    await resHumans[0].click(e.chat_id, silent=True, hide_via=True)
    await e.delete()


@in_pattern("calc")
@in_owner
async def _(e):
    m = [
        "AC",
        "C",
        "⌫",
        "%",
        "7",
        "8",
        "9",
        "+",
        "4",
        "5",
        "6",
        "-",
        "1",
        "2",
        "3",
        "x",
        "00",
        "0",
        ".",
        "÷",
    ]
    tHumand = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
    lst = list(zip(tHumand[::4], tHumand[1::4], tHumand[2::4], tHumand[3::4]))
    lst.append([Button.inline("=", data="calc=")])
    calc = e.builder.article("Calc", text="• Humanoid Inline Calculator •", buttons=lst)
    await e.answer([calc])


@callback(re.compile("calc(.*)"))
@owner
async def _(e):
    x = (e.data_match.group(1)).decode()
    if x == "AC":
        HumandB.delete("calc")
        return await e.edit(
            "• Humanoid Inline Calculator •",
            buttons=[Button.inline("Open Calculator Again", data="recalc")],
        )
    elif x == "C":
        HumandB.delete("calc")
        return await e.answer("cleared")
    elif x == "⌫":
        get = HumandB.get("calc")
        if get:
            HumandB.set("calc", get[:-1])
            return await e.answer(str(get[:-1]))
    elif x == "%":
        get = HumandB.get("calc")
        if get:
            HumandB.set("calc", get + "/100")
            return await e.answer(str(get + "/100"))
    elif x == "÷":
        get = HumandB.get("calc")
        if get:
            HumandB.set("calc", get + "/")
            return await e.answer(str(get + "/"))
    elif x == "x":
        get = HumandB.get("calc")
        if get:
            HumandB.set("calc", get + "*")
            return await e.answer(str(get + "*"))
    elif x == "=":
        get = HumandB.get("calc")
        if get:
            if get.endswith(("*", ".", "/", "-", "+")):
                get = get[:-1]
            out = await calcc(get, e)
            try:
                num = float(out)
                return await e.answer(f"Answer : {num}", cache_time=0, alert=True)
            except BaseException:
                HumandB.delete("calc")
                return await e.answer("Error", cache_time=0, alert=True)
        return await e.answer("None")
    else:
        get = HumandB.get("calc")
        if get:
            HumandB.set("calc", get + x)
            return await e.answer(str(get + x))
        HumandB.set("calc", x)
        return await e.answer(str(x))


@callback("recalc")
@owner
async def _(e):
    m = [
        "AC",
        "C",
        "⌫",
        "%",
        "7",
        "8",
        "9",
        "+",
        "4",
        "5",
        "6",
        "-",
        "1",
        "2",
        "3",
        "x",
        "00",
        "0",
        ".",
        "÷",
    ]
    tHumand = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
    lst = list(zip(tHumand[::4], tHumand[1::4], tHumand[2::4], tHumand[3::4]))
    lst.append([Button.inline("=", data="calc=")])
    await e.edit("Noice Inline Calculator", buttons=lst)
