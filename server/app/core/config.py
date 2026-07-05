import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings:

    TRANSLATION_PROVIDER = os.getenv(
        "TRANSLATION_PROVIDER",
        "mock"
    )

    OPENROUTER_API_KEY = os.getenv(
        "OPENROUTER_API_KEY",
        ""
    )

    OPENROUTER_MODEL = os.getenv(
        "OPENROUTER_MODEL",
        "google/gemma-3-27b-it:free"
    )


print("API Key Loaded:", bool(Settings.OPENROUTER_API_KEY))

settings = Settings()