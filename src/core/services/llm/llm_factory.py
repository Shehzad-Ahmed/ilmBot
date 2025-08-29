from enum import Enum

from src.core.services.llm.providers import OpenRouterLLM


class LLMProvider(Enum):
    OPENROUTER = "openrouter"

    @classmethod
    def list_providers(cls):
        return [provider.value for provider in cls]


class LLMFactory:
    """
    Factory class for creating LLMs,
    Any new provider should be added here.
    """

    Provider = LLMProvider

    @classmethod
    def create_llm(
        cls,
        provider: LLMProvider,
        model_name: str,
        temperature: float = None,
        top_p: float = None,
    ):
        if provider not in cls.Provider:
            raise ValueError(
                f"Invalid provider. Must be one of: {cls.Provider.list_providers()}"
            )
        if provider == cls.Provider.OPENROUTER:
            return OpenRouterLLM(model_name, temperature, top_p)
        raise ValueError(f"Unknown provider: {provider}")
