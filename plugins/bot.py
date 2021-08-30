# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available

• `{i}alive`
    Check if your bot is working.

• `{i}ping`
    Check Humanoid's response time.

• `{i}cmds`
    View all plugin names.

• `{i}restart`
    To restart your bot.

• `{i}logs (sys)`
    Get the full terminal logs.

• `{i}logs heroku`
   Get the latest 100 lines of heroku logs.

• `{i}shutdown`
    Turn off your bot.
"""
import time
from datetime import datetime as dt
from platform import python_version as pyver

from git import Repo
from pyHumanoid.version import __version__ as UltVer
from telethon import __version__, events
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

from . import *


@Humanoid_cmd(
    pattern="alive$",
)
async def lol(Human):
    pic = HumandB.get("ALIVE_PIC")
    uptime = time_formatter((time.time() - start_time) * 1000)
    header = (
        HumandB.get("ALIVE_TEXT") if HumandB.get("ALIVE_TEXT") else "Hey,  I am alive."
    )
    y = Repo().active_branch
    xx = Repo().remotes[0].config_reader.get("url")
    rep = xx.replace(".git", f"/tree/{y}")
    kk = f" `[{y}]({rep})` "
    als = (get_string("alive_1")).format(
        header,
        OWNER_NAME,
        Humanoid_version,
        UltVer,
        uptime,
        pyver(),
        __version__,
        kk,
    )
    if pic is None:
        return await eor(Human, als)
    elif pic is not None and "telegra" in pic:
        try:
            await Human.reply(als, file=pic, link_preview=False)
            await Human.delete()
        except ChatSendMediaForbiddenError:
            await eor(Human, als, link_preview=False)
    else:
        try:
            await Human.reply(file=pic)
            await Human.reply(als, link_preview=False)
            await Human.delete()
        except ChatSendMediaForbiddenError:
            await eor(Human, als, link_preview=False)


@Humanoid_bot.on(events.NewMessage(pattern=f"\\{HNDLR}ping$"))
async def _(event):
    if event.fwd_from:
        return
    if not event.out and not is_sudo(event.sender_id):
        return
    start = dt.now()
    x = await eor(event, "`Pong !`")
    end = dt.now()
    ms = (end - start).microseconds / 1000
    uptime = time_formatter((time.time() - start_time) * 1000)
    await x.edit(get_string("ping").format(ms, uptime))


@Humanoid_cmd(
    pattern="cmds$",
)
async def cmds(event):
    await allcmds(event)


@Humanoid_cmd(
    pattern="restart$",
)
async def restartbt(Human):
    ok = await eor(Human, "`Restarting...`")
    if Var.HEROKU_API:
        await restart(ok)
    else:
        await bash("pkill python3 && python3 -m pyHumanoid")


@Humanoid_cmd(pattern="shutdown$")
async def shutdownbot(Human):
    if not Human.out and not is_fullsudo(Human.sender_id):
        return await eod(Human, "`This Command Is Sudo Restricted.`")
    await shutdown(Human)


@Humanoid_bot.on(events.NewMessage(pattern=f"\\{HNDLR}logs ?(.*)"))
@asst.on(events.NewMessage(pattern="^/{HNDLR}logs ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.out and not is_sudo(event.sender_id):
        return
    try:
        opt = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await def_logs(event)
    if opt == "heroku":
        await heroku_logs(event)
    else:
        await def_logs(event)
    if event.out:
        await event.delete()
