import os

from app.providers.base import LLMProvider
from app.providers.embedding_base import EmbeddingProvider
from app.providers.ollama import OllamaProvider
from app.providers.ollama_embedding import OllamaEmbeddingProvider

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3:3.8b")
OLLAMA_EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")


def get_llm_provider() -> LLMProvider:
    if LLM_PROVIDER == "ollama":
        return OllamaProvider(base_url=OLLAMA_BASE_URL, model=OLLAMA_MODEL)
    raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")


def get_embedding_provider() -> EmbeddingProvider:
    if LLM_PROVIDER == "ollama":
        return OllamaEmbeddingProvider(base_url=OLLAMA_BASE_URL, model=OLLAMA_EMBEDDING_MODEL)
    raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")
