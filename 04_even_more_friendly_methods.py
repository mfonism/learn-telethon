from telethon import TelegramClient

import settings

client = TelegramClient(
    settings.USER_SESSION_FILENAME, settings.API_ID, settings.API_HASH
)


async def main():
    async for dialog in client.iter_dialogs():
        print(dialog.name, "has ID", dialog.id)

    text = (
        f"Hi Kiwi\n\n"
        f"This message has **bold**, __italics__, `code`, and"
        f" a [hyperlink](https://mfonism.pythonanywhere.com)"
    )
    message = await client.send_message("me", text)
    await message.reply("Oh, and this is a reply!")


with client:
    client.loop.run_until_complete(main())
