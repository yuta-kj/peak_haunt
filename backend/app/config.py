import os

from app.providers.base import LLMProvider
from app.providers.ollama import OllamaProvider

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3:3.8b")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")


def get_llm_provider() -> LLMProvider:
    if LLM_PROVIDER == "ollama":
        return OllamaProvider(base_url=OLLAMA_BASE_URL, model=OLLAMA_MODEL)
    raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")
