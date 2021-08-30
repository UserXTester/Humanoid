# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available

•`{i}invertgif`
  Make Gif Inverted(negative).

•`{i}bwgif`
  Make Gif black and white

•`{i}vtog`
  Reply To Video , It will Create Gif
  Video to Gif

•`{i}gif <query>`
   Send video regarding to query.
"""
import os
import random
import time
from datetime import datetime as dt

from . import *


@Humanoid_cmd(pattern="bwgif$")
async def igif(e):
    a = await e.get_reply_message()
    if not (a and a.media):
        return await eod(e, "`Reply To gif only`")
    wut = mediainfo(a.media)
    if "gif" not in wut:
        return await eod(e, "`Reply To Gif Only`")
    xx = await eor(e, "`Processing...`")
    z = await a.download_media()
    try:
        await bash(f'ffmpeg -i "{z}" -vf format=gray Human.gif -y')
        await e.client.send_file(e.chat_id, "Human.gif", support_stream=True)
        os.remove(z)
        os.remove("Human.gif")
        await xx.delete()
    except Exception as er:
        LOGS.info(er)


@Humanoid_cmd(pattern="invertgif$")
async def igif(e):
    a = await e.get_reply_message()
    if not (a and a.media):
        return await eod(e, "`Reply To gif only`")
    wut = mediainfo(a.media)
    if "gif" not in wut:
        return await eod(e, "`Reply To Gif Only`")
    xx = await eor(e, "`Processing...`")
    z = await a.download_media()
    try:
        await bash(
            f'ffmpeg -i "{z}" -vf lutyuv="y=negval:u=negval:v=negval" Human.gif -y'
        )
        await e.client.send_file(e.chat_id, "Human.gif", support_stream=True)
        os.remove(z)
        os.remove("Human.gif")
        await xx.delete()
    except Exception as er:
        LOGS.info(er)


@Humanoid_cmd(pattern="gif ?(.*)")
async def gifs(Human):
    get = Human.pattern_match.group(1)
    xx = random.randint(0, 5)
    n = 0
    if ";" in get:
        try:
            n = int(get.split(";")[-1])
        except BaseException:
            pass
    if not get:
        return await eor(Human, f"`{HNDLR}gif <query>`")
    m = await eor(Human, "`Searching gif ...`")
    gifs = await Human.client.inline_query("gif", get)
    if not n:
        await gifs[xx].click(
            Human.chat.id, reply_to=Human.reply_to_msg_id, silent=True, hide_via=True
        )
    else:
        for x in range(n):
            await gifs[x].click(
                Human.chat.id,
                reply_to=Human.reply_to_msg_id,
                silent=True,
                hide_via=True,
            )
    await m.delete()


@Humanoid_cmd(pattern="vtog$")
async def vtogif(e):
    a = await e.get_reply_message()
    if not (a and a.media):
        return await eod(e, "`Reply To video only`")
    wut = mediainfo(a.media)
    if "video" not in wut:
        return await eod(e, "`Reply To Video Only`")
    xx = await eor(e, "`Processing...`")
    dur = a.media.document.attributes[0].duration
    tt = time.time()
    if int(dur) < 120:
        z = await a.download_media()
        await bash(
            f'ffmpeg -i {z} -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 Human.gif -y'
        )
        await e.client.send_file(e.chat_id, "Human.gif", support_stream=True)
        os.remove(z)
        os.remove("Human.gif")
        await xx.delete()
    else:
        filename = a.file.name
        if not filename:
            filename = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
        vid = await downloader(filename, a.media.document, xx, tt, "Downloading...")
        z = vid.name
        await bash(
            f'ffmpeg -ss 3 -t 100 -i {z} -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 Human.gif'
        )
        await e.client.send_file(e.chat_id, "Human.gif", support_stream=True)
        os.remove(z)
        os.remove("Human.gif")
        await xx.delete()
