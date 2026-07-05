from abc import ABC, abstractmethod


class SpeechProvider(ABC):

    @abstractmethod
    def transcribe(self, audio_file: str) -> str:
        pass