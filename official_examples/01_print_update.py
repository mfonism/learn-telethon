from telethon import TelegramClient

import settings

client = TelegramClient(
    settings.USER_SESSION_FILENAME, settings.API_ID, settings.API_HASH
)


async def handler(update):
    print(update)


with client:
    client.add_event_handler(handler)
    print("Running telegram client...")
    print("(Press 'Ctrl + C' to terminate this session)")
    client.run_until_disconnected()
