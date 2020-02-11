import logging

from telethon import TelegramClient, events

import settings

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

client = TelegramClient(
    settings.USER_SESSION_FILENAME, settings.API_ID, settings.API_HASH
)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if "Kiwi" in event.raw_text:
        await event.reply("Yas, boo!")


client.start()
client.run_until_disconnected()
