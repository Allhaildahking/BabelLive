from abc import ABC, abstractmethod


class TTSProvider(ABC):

    @abstractmethod
    def speak(self, text: str) -> str:
        """
        Converts text into speech.

        Returns:
            Path to generated audio file.
        """
        pass