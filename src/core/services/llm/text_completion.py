from src.core.services.llm.base import BaseLLM
from src.core.services.llm.llm_factory import LLMFactory


class TextCompletionLLM(BaseLLM):
    _instance_cache = {}

    def __new__(
        cls,
        provider: LLMFactory.Provider = LLMFactory.Provider.OPENROUTER,
        model_name: str = "gpt-3.5-turbo",
        prompt_template: str = "Complete this text appropriately for: {text}",
        temperature: float = 0.7,  # For balanced results
        top_p: float = None,
    ):
        cache_key = (provider, model_name, temperature, top_p)
        if cache_key not in cls._instance_cache:
            instance = super().__new__(cls)
            instance._initialize(
                provider, model_name, prompt_template, temperature, top_p
            )
            cls._instance_cache[cache_key] = instance
        return cls._instance_cache[cache_key]
