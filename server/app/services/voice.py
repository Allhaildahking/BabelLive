from app.core.config import settings


class VoiceService:

    def __init__(self):

        if settings.TTS_PROVIDER == "elevenlabs":
            from app.services.providers.elevenlabs import ElevenLabsProvider
            self.provider = ElevenLabsProvider()
        else:
            raise ValueError("Unsupported TTS provider")

    def speak(self, text: str):
        return self.provider.speak(text)