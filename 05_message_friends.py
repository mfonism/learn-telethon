from telethon import TelegramClient

import settings

client = TelegramClient(
    settings.USER_SESSION_FILENAME, settings.API_ID, settings.API_HASH
)


async def main():
    txt_to_dan = (
        "Hi Dan, this is me chatting you from a Python script I created last night."
    )
    # can chat with someone using their ID
    msg_to_dan = await client.send_message(1052571690, txt_to_dan)
    await msg_to_dan.reply(
        "Please send me a screenshot of this chat so I know how it appears at your end."
    )

    # can also chat with someone using their Phone Number
    txt_to_kene = (
        "Hi Kene, this is me chatting you from Python script I created last night."
    )
    msg_to_kene = await client.send_message("+2349051687007", txt_to_kene)
    await msg_to_kene.reply(
        "Please send me a screenshot of this chat so I know how it appears at your end."
    )

    # their username, too
    txt_to_kiwi = (
        "Hi Kiwi, this is me chatting you from Python script I created last night."
    )
    msg_to_kiwi = await client.send_message("@mfonism", txt_to_kiwi)
    await msg_to_kiwi.reply(
        "Please send me a screenshot of this chat so I know how it appears at your end."
    )


with client:
    client.loop.run_until_complete(main())
