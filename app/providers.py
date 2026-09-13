from abc import ABC, abstractmethod
from app.models import Episode

class TextGenerator(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str: ...

class VoiceGenerator(ABC):
    @abstractmethod
    def synthesize(self, text: str, output_path: str) -> str: ...

class VisualGenerator(ABC):
    @abstractmethod
    def generate(self, prompt: str, output_path: str) -> str: ...

class YouTubePublisher(ABC):
    @abstractmethod
    def upload(self, episode: Episode, video_path: str) -> str: ...

class DemoTextGenerator(TextGenerator):
    def generate(self, prompt: str) -> str:
        return f"DEMO OUTPUT: {prompt}"

class DisabledPublisher(YouTubePublisher):
    def upload(self, episode: Episode, video_path: str) -> str:
        raise RuntimeError("Publishing is disabled. Configure and validate YouTube OAuth first.")
