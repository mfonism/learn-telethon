from telethon import TelegramClient, events, utils

import settings

client = TelegramClient(
    settings.USER_SESSION_FILENAME, settings.API_ID, settings.API_HASH
).start()

# handle an event of a new message
# containing a case case-insensitive 'hello' or 'hi'
@client.on(events.NewMessage(pattern=r"(?i).*\b(hello|hi)\b"))
async def handler(event):
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    print(f"{name} said {event.text}!")


with client:
    print("Running telegram client...")
    print("(Press 'Ctrl + C' to terminate this session)")
    client.run_until_disconnected()
