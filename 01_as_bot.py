from telethon.sync import TelegramClient

import settings


async def display_obj_dir(obj):
    from pprint import pprint

    pprint(dir(obj))


with TelegramClient(
    settings.BOT_SESSION_FILENAME, settings.API_ID, settings.API_HASH
).start(bot_token=settings.BOT_TOKEN) as bot:
    bot.loop.run_until_complete(display_obj_dir(bot))
