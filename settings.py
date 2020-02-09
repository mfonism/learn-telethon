import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(".").absolute()

load_dotenv(BASE_DIR.joinpath(".env"))

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

SESSION_FILENAME = str(BASE_DIR.joinpath("secret.session"))
