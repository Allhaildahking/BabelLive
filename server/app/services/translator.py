from app.core.config import settings
from app.services.providers.mock import MockTranslationProvider
from app.services.providers.libretranslate import LibreTranslateProvider
from app.services.providers.openrouter import OpenRouterProvider


class TranslatorService:

    def __init__(self):

        if settings.TRANSLATION_PROVIDER == "mock":
            self.provider = MockTranslationProvider()

        elif settings.TRANSLATION_PROVIDER == "libretranslate":
            self.provider = LibreTranslateProvider()

        elif settings.TRANSLATION_PROVIDER == "openrouter":
            self.provider = OpenRouterProvider()

        else:
            raise ValueError(
                f"Unknown provider: {settings.TRANSLATION_PROVIDER}"
            )

    def translate(self, text: str, target_language: str = "es") -> str:
        return self.provider.translate(text, target_language)