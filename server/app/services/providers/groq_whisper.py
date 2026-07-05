from openai import OpenAI

from app.core.config import settings
from app.services.providers.speech_base import SpeechProvider


class GroqWhisperProvider(SpeechProvider):

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

        self.model = settings.GROQ_WHISPER_MODEL

    def transcribe(self, audio_file: str) -> str:

        with open(audio_file, "rb") as file:

            transcription = self.client.audio.transcriptions.create(
                model=self.model,
                file=file
            )

        return transcription.text