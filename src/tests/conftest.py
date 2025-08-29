import pytest
from unittest.mock import patch

from fastapi.testclient import TestClient
from langchain_core.outputs import LLMResult, ChatGeneration
from langchain_core.messages import AIMessage

from src.core.config import Settings, get_settings
from src.main import app


@pytest.fixture
def client():
    """Fixture that provides a test client for the FastAPI application."""

    return TestClient(app)


@pytest.fixture(autouse=True)
def override_get_settings():
    def get_settings_override():
        return Settings(
            ENV="test",
            OPENROUTER_API_BASE_URL="https://openrouter.ai/api/v1",
            OPENROUTER_API_KEY="test_api_key",
        )

    app.dependency_overrides[get_settings] = get_settings_override
    yield
    app.dependency_overrides = {}


@pytest.fixture
def mock_chat_openai_agenerate():
    with patch("langchain_openai.chat_models.ChatOpenAI.agenerate") as mock:
        yield mock


@pytest.fixture
def create_mock_llm_result():
    """Fixture to create a mock LLMResult with the given text"""

    def llm_result(texts: list[str]) -> LLMResult:
        return LLMResult(
            generations=[
                [
                    ChatGeneration(text=text, message=AIMessage(content=text))
                    for text in texts
                ]
            ],
            llm_output={},
        )

    return llm_result
