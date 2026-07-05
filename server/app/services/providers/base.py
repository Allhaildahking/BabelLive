from abc import ABC, abstractmethod


class TranslationProvider(ABC):

    @abstractmethod
    def translate(self, text: str, target_language: str = "es") -> str:
        """Translate text into the target language."""
        pass