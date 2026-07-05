from app.core.config import settings
from app.services.providers.groq_whisper import GroqWhisperProvider


class SpeechService:

    def __init__(self):

        if settings.SPEECH_PROVIDER == "groq":
            self.provider = GroqWhisperProvider()
        else:
            raise ValueError(
                f"Unknown speech provider: {settings.SPEECH_PROVIDER}"
            )

    def transcribe(self, audio_file: str) -> str:
        return self.provider.transcribe(audio_file)