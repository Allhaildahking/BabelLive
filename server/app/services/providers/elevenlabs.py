from elevenlabs.client import ElevenLabs
from app.core.config import settings


class ElevenLabsProvider:

    def __init__(self):
        self.client = ElevenLabs(
            api_key=settings.ELEVENLABS_API_KEY
        )

        self.voice_id = settings.ELEVENLABS_VOICE_ID

    def speak(self, text: str):

        audio = self.client.text_to_speech.convert(
            voice_id=self.voice_id,
            text=text,
            model_id="eleven_multilingual_v2"
        )

        output_file = "outputs/translated.mp3"

        import os
        os.makedirs("outputs", exist_ok=True)

        with open(output_file, "wb") as f:
            for chunk in audio:
                if chunk:
                    f.write(chunk)

        return output_file