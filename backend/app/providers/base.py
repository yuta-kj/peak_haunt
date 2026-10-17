from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator


class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass

    @abstractmethod
    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        yield  # type: ignore[misc]
