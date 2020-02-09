from telethon import TelegramClient

import settings

client = TelegramClient(
    settings.USER_SESSION_FILENAME, settings.API_ID, settings.API_HASH
)


async def main():
    me = await client.get_me()

    print("Pretty Printed Me:")
    print(me.stringify())

    print()
    print("Methods on Me:")
    print(
        [
            field
            for field in dir(me)
            if (callable(getattr(me, field)) and not field.startswith("_"))
        ]
    )


with client:
    client.loop.run_until_complete(main())
