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
        "google/gemma-3-27b-it"
    )

    SPEECH_PROVIDER = os.getenv(
        "SPEECH_PROVIDER",
        "groq"
    )

    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY",
        ""
    )

    GROQ_WHISPER_MODEL = os.getenv(
        "GROQ_WHISPER_MODEL",
        "whisper-large-v3-turbo"
    )

    TTS_PROVIDER = os.getenv(
        "TTS_PROVIDER",
        "elevenlabs"
    )

    ELEVENLABS_API_KEY = os.getenv(
        "ELEVENLABS_API_KEY",
        ""
    )

    ELEVENLABS_VOICE_ID = os.getenv(
        "ELEVENLABS_VOICE_ID",
        "EXAVITQu4vr4xnSDxMaL"
    )


settings = Settings()

print("API Key Loaded:", bool(settings.OPENROUTER_API_KEY))
print("Groq Key Loaded:", bool(settings.GROQ_API_KEY))
print("ElevenLabs Key Loaded:", bool(settings.ELEVENLABS_API_KEY))