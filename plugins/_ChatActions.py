from pyHumanoid.functions.all import get_chatbot_reply
from pyHumanoid.functions.chatBot_db import chatbot_stats
from pyHumanoid.functions.clean_db import *
from pyHumanoid.functions.forcesub_db import *
from pyHumanoid.functions.gban_mute_db import *
from pyHumanoid.functions.greetings_db import *
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.utils import get_display_name

from . import *
# Phoenix Error

@Humanoid_bot.on(events.ChatAction())
async def ChatActionsHandler(Human):  # sourcery no-metrics
    # clean chat actions
    if is_clean_added(Human.chat_id):
        try:
            await Human.delete()
        except BaseException:
            pass

    # thank members
    if must_thank(Human.chat_id):
        chat_count = len(await Human.client.get_participants(await Human.get_chat()))
        if chat_count % 100 == 0:
            stik_id = chat_count / 100 - 1
            sticker = stickers[stik_id]
            await Humanoid.send_message(Human.chat_id, file=sticker)
    # force subscribe
    if (
        HumandB.get("FORCESUB")
        and ((Human.user_joined or Human.user_added))
        and get_forcesetting(Human.chat_id)
    ):
        user = await Human.get_user()
        if not user.bot:
            joinchat = get_forcesetting(Human.chat_id)
            try:
                await Humanoid_bot(GetParticipantRequest(int(joinchat), user.id))
            except UserNotParticipantError:
                await Humanoid_bot.edit_permissions(
                    Human.chat_id, user.id, send_messages=False
                )
                res = await Humanoid_bot.inline_query(
                    asst.me.username, f"fsub {user.id}_{joinchat}"
                )
                await res[0].click(Human.chat_id, reply_to=Human.action_message.id)

    # gban checks
    if Human.user_joined and Human.added_by:
        user = await Human.get_user()
        chat = await Human.get_chat()
        if is_gbanned(str(user.id)) and chat.admin_rights:
            try:
                await Humanoid_bot.edit_permissions(
                    chat.id,
                    user.id,
                    view_messages=False,
                )
                reason = get_gban_reason(user.id)
                gban_watch = f"#GBanned_User Joined.\n\n**User** - [{user.first_name}](tg://user?id={user.id})\n"
                if reason is not None:
                    gban_watch += f"**Reason**: {reason}\n\n"
                gban_watch += f"`User Banned.`"
                await Human.reply(gban_watch)
            except BaseException:
                pass

        # greetings
        if get_welcome(Human.chat_id):
            user = await Human.get_user()
            chat = await Human.get_chat()
            title = chat.title or "this chat"
            pp = await Human.client.get_participants(chat)
            count = len(pp)
            mention = f"[{get_display_name(user)}](tg://user?id={user.id})"
            name = user.first_name
            last = user.last_name
            fullname = f"{name} {last}" if last else name
            uu = user.username
            username = f"@{uu}" if uu else mention
            msgg = wel["welcome"]
            med = wel["media"]
            userid = user.id
            if msgg and not is_gbanned(str(user.id)):
                send = await Human.reply(
                    msgg.format(
                        mention=mention,
                        group=title,
                        count=count,
                        name=name,
                        fullname=fullname,
                        username=username,
                        userid=userid,
                    ),
                    file=med,
                )
                await asyncio.sleep(150)
                await send.delete()
            elif not is_gbanned(str(user.id)):
                await Human.reply(file=med)
    if (Human.user_left or Human.user_kicked) and get_goodbye(Human.chat_id):
        user = await Human.get_user()
        chat = await Human.get_chat()
        title = chat.title or "this chat"
        pp = await Human.client.get_participants(chat)
        count = len(pp)
        mention = f"[{get_display_name(user)}](tg://user?id={user.id})"
        name = user.first_name
        last = user.last_name
        fullname = f"{name} {last}" if last else name
        uu = user.username
        username = f"@{uu}" if uu else mention
        msgg = wel["goodbye"]
        med = wel["media"]
        userid = user.id
        if msgg:
            send = await Human.reply(
                msgg.format(
                    mention=mention,
                    group=title,
                    count=count,
                    name=name,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                ),
                file=med,
            )
            await asyncio.sleep(150)
            await send.delete()
        else:
            await Human.reply(file=med)


@Humanoid_bot.on(events.NewMessage(incoming=True))
async def chatBot_replies(event):
    if event.sender_id and chatbot_stats(event.chat_id, event.sender_id) and not event.media:
        msg = get_chatbot_reply(event, event.text)
        if msg:
            await event.reply(msg)
