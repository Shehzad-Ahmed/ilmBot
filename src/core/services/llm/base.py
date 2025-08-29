import asyncio

from typing import AsyncGenerator

from src.core.services.llm.llm_factory import LLMFactory


class BaseLLM:
    """Abstract base class for LLM summarization implementations."""

    def _initialize(
        self,
        provider: LLMFactory.Provider,
        model_name: str,
        prompt_template: str,
        temperature: float,
        top_p: float,
    ):
        self.provider = provider
        self.model_name = model_name
        self.prompt_template = prompt_template
        self.temperature = temperature
        self.top_p = top_p
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = LLMFactory.create_llm(
                self.provider, self.model_name, self.temperature, self.top_p
            ).get_client()
        return self._client

    async def stream_response(self, text: str) -> AsyncGenerator[str, None]:
        response = await self.client.agenerate(
            messages=[self.prompt_template.format(text=text)]
        )

        for chunk in response.generations[0]:
            yield chunk.text
            await asyncio.sleep(0.02)  # Small delay for smoother streaming
