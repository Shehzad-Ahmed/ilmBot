from langchain_openai.chat_models import ChatOpenAI
from src.core.services.llm.providers.base import BaseLLMProvider
from src.core import get_settings

settings = get_settings()


class OpenRouterLLM(BaseLLMProvider):
    def __init__(
        self,
        model_name: str,
        temperature: float = None,
        top_p: float = None,
        stream=True,
    ):
        self.model_name = model_name
        self.stream = stream
        self.extra_args = {}
        if temperature is not None:
            self.extra_args["temperature"] = temperature
        if top_p is not None:
            self.extra_args["top_p"] = top_p

    def get_client(self):
        return ChatOpenAI(
            model=self.model_name,
            max_retries=2,
            api_key=settings.OPENROUTER_API_KEY,
            base_url=settings.OPENROUTER_API_BASE_URL,
            # model_kwargs={"stream": self.stream},
            stream_options={"include_usage": self.stream},
            **self.extra_args
        )

    def get_model_name(self) -> str:
        return self.model_name

    def get_extra_args(self) -> dict:
        return self.extra_args
