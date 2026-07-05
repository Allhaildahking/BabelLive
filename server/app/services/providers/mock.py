from app.services.providers.base import TranslationProvider


class MockTranslationProvider(TranslationProvider):

    def translate(self, text: str, target_language: str = "es") -> str:

        translations = {
            "Good morning everyone": "Buenos días a todos.",
            "Hello": "Hola",
            "Welcome to church": "Bienvenidos a la iglesia",
            "Jesus loves you": "Jesús te ama"
        }

        return translations.get(
            text,
            f"[Spanish Translation] {text}"
        )