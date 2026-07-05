import requests

from app.services.providers.base import TranslationProvider


class LibreTranslateProvider(TranslationProvider):

    def __init__(self):
        self.url = "https://libretranslate.com/translate"

    def translate(self, text: str, target_language: str = "es") -> str:

        payload = {
            "q": text,
            "source": "en",
            "target": target_language,
            "format": "text"
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            return data["translatedText"]

        except Exception as e:
            return f"Translation Error: {str(e)}"