# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• {i}unsplash <search query> ; <no of pics>
    Unsplash Image Search.

"""
import urllib

import requests as r
from bs4 import BeautifulSoup as bs

from . import *


@Humanoid_cmd(pattern="unsplash ?(.*)")
async def searchunsl(Human):
    match = Human.pattern_match.group(1)
    if not match:
        return await eor(Human, "Give me Something to Search")
    if ";" in match:
        num = int(match.split(";")[1])
        query = match.split(";")[0]
    else:
        num = 5
        query = match
    tep = await eor(Human, "`Processing... `")
    res = autopicsearch(query)
    if len(res) == 0:
        return await eod(Human, "No ResHumans Found !")
    qas = res[:num]
    dir = "resources/downloads"
    CL = []
    nl = 0
    for rp in qas:
        li = "https://unsplash.com" + rp["href"]
        ct = r.get(li).content
        bst = bs(ct, "html.parser", from_encoding="utf-8")
        ft = bst.find_all("img", "_2UpQX")[0]["src"]
        Hp = dir + "img" + f"{nl}.png"
        urllib.request.urlretrieve(ft, Hp)
        CL.append(Hp)
        nl += 1
    await Human.client.send_file(
        Human.chat_id, CL, caption=f"Uploaded {len(qas)} Images\n", album=True
    )
    await tep.delete()
