# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}autopic <search query>`
    Will change your profile pic at defined intervals with pics related to the given topic.

• `{i}stoppic`
    Stop the AutoPic command.

"""
import asyncio
import os
import urllib

import requests as r
from bs4 import BeautifulSoup as bs
from telethon.tl.functions.messages import GetWebPagePreviewRequest as getweb
from telethon.tl.functions.photos import UploadProfilePhotoRequest

from . import *


@Humanoid_cmd(pattern="autopic ?(.*)")
async def autopic(e):
    search = e.pattern_match.group(1)
    if not search:
        return await eod(e, get_string("autopic_1"))
    clls = autopicsearch(search)
    if len(clls) == 0:
        return await eod(e, get_string("autopic_2").format(search))
    await eor(e, get_string("autopic_3").format(search))
    HumandB.set("AUTOPIC", "True")
    ST = HumandB.get("SLEEP_TIME")
    if ST:
        SLEEP_TIME = int(ST)
    else:
        SLEEP_TIME = 1221
    while True:
        for lie in clls:
            ge = HumandB.get("AUTOPIC")
            if not ge == "True":
                return
            au = "https://unsplash.com" + lie["href"]
            et = await e.client(getweb(au))
            try:
                kar = await e.client.download_media(et.webpage.photo)
            except AttributeError:
                ct = r.get(au).content
                bsc = bs(ct, "html.parser", from_encoding="utf-8")
                ft = bsc.find_all("img", "_2UpQX")
                li = ft[0]["src"]
                kar = "autopic.png"
                urllib.request.urlretrieve(li, kar)
            file = await e.client.upload_file(kar)
            await e.client(UploadProfilePhotoRequest(file))
            os.remove(kar)
            await asyncio.sleep(SLEEP_TIME)


@Humanoid_cmd(pattern="stoppic$")
async def stoppo(ult):
    gt = HumandB.get("AUTOPIC")
    if not gt == "True":
        return await eod(ult, "AUTOPIC was not in used !!")
    HumandB.set("AUTOPIC", "None")
    await eod(ult, "AUTOPIC Stopped !!")
