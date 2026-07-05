from openai import OpenAI

from app.core.config import settings
from app.services.providers.base import TranslationProvider


class OpenRouterProvider(TranslationProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

        self.model = settings.OPENROUTER_MODEL

    def translate(self, text: str, target_language: str = "es") -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a professional translator. Translate everything into {target_language}. Return ONLY the translated text."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content.strip()