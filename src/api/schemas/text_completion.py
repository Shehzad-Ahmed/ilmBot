from pydantic import BaseModel, Field


class TextCompletionRequest(BaseModel):
    """
    Text Completion endpoint schema. The length of the prompt is limited to 10,000 characters.
    Which can approximate to 1500 words. Further the limit will be tested based on token count.
    """

    text: str = Field(
        description="prompt to summarise. Max length 10,000 characters",
        max_length=10000,
    )
