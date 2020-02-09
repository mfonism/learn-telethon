from telethon import TelegramClient

import settings

client = TelegramClient(
    settings.USER_SESSION_FILENAME, settings.API_ID, settings.API_HASH
)


async def main():
    print("Methods on Client")
    print(
        [
            field
            for field in dir(client)
            if (callable(getattr(client, field)) and not field.startswith("_"))
        ]
    )

    print()
    print("Attributes on Client")
    print(
        [
            field
            for field in dir(client)
            if (not callable(getattr(client, field)) and not field.startswith("_"))
        ]
    )


with client:
    client.loop.run_until_complete(main())
