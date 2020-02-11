import logging
import time
from collections import defaultdict

from telethon import TelegramClient, events

import settings

logging.basicConfig(level=logging.WARNING)

# when did we last react?
# Dict[ChatID, MostRecentReactTime]
recent_reacts = defaultdict(float)


def can_react(chat_id):
    now = time.time()
    mrrt = recent_reacts[chat_id]

    if now - mrrt < 10 * 60:
        recent_reacts[chat_id] = now
        return True
    return False


@events.register(events.NewMessage)
async def handler(event):
    if not event.out:
        if "emacs" in event.raw_text:
            if can_react(event.chat_id):
                await event.reply("> emacs\nneeds more vim")
        elif "vim" in event.raw_text:
            if can_react(event.chat_id):
                await event.reply("> vim\nneeds more emacs")
        elif "chrome" in event.raw_text:
            if can_react(event.chat_id):
                await event.reply("> chrome\nneeds more firefox")

    if "shrug" in event.raw_text:
        if can_react(event.chat_id):
            await event.respond(r"¯\_(ツ)_/¯")

    # the event has a reference to the client
    # so we can inspect the client in the handler
    client = event.client

    if event.out and event.reply_to_msg_id and "save pic" in event.raw_text:
        reply_msg = await event.get_reply_message()
        replied_to_user = await reply_msg.get_input_sender()

        message = await event.reply("Downloading your profile photo...")
        file = await client.download_profile_photo(replied_to_user)
        await message.edit(f"I saved your photo in {file}")


client = TelegramClient(
    settings.USER_SESSION_FILENAME, settings.API_ID, settings.API_HASH
)

with client:
    # this remembers the events.NewMessage we registered
    client.add_event_handler(handler)
    print("Running telegram client...")
    print("(Press 'Ctrl + C' to terminate this session)")
    client.run_until_disconnected()
