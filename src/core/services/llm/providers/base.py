from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    The Provider Interface, a base class for all LLM providers.
    """

    @abstractmethod
    def get_client(self):
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        pass

    @abstractmethod
    def get_extra_args(self) -> str:
        pass
