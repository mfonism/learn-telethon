import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(".").absolute()

load_dotenv(BASE_DIR.joinpath(".env"))

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

BOT_TOKEN = os.getenv("BOT_TOKEN")

USER_SESSION_FILENAME = str(BASE_DIR.joinpath("secret"))
BOT_SESSION_FILENAME = str(BASE_DIR.joinpath("bot"))
