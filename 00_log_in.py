from telethon import TelegramClient

import settings

with TelegramClient(
    settings.SESSION_FILENAME, settings.API_ID, settings.API_HASH,
) as client:
    client.loop.run_until_complete(client.send_message("me", "Hi Kiwi!"))
