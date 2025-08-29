from typing import Union

from fastapi import APIRouter, status, Request
from fastapi.responses import StreamingResponse, JSONResponse

from src.api.schemas import TextCompletionRequest, error_responses
from src.core.limiter import get_limiter
from src.core.services.llm import TextCompletionLLM
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1", tags=["Text Completion"])

limiter = get_limiter()


class TextCompletionSuccessResponse(BaseModel):
    """Successful streaming response model"""

    content: str
    media_type: str = "text/plain"


@router.post(
    "/text-completion",
    response_class=StreamingResponse,
    responses={
        **error_responses,
        200: {
            "content": {"text/event-stream": {}},
            "description": "Successful streaming response",
        },
    },
    response_model=TextCompletionSuccessResponse,
    summary="Stream text summarisation",
    description="Streams text completion in real-time using LLMs",
)
@limiter.limit("20/minute")
async def text_completion(
    request: Request,
    request_obj: TextCompletionRequest,
) -> Union[StreamingResponse, JSONResponse]:
    """
    Text completes input text using a Language Model (LLM) and streams
    the output in real-time using Server-Sent Events (SSE).

    Returns either:
    - 200: Successful text stream (text/plain)
    - 4XX/5XX: JSON error response (application/json)
    """
    text = request_obj.text
    if not text:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "detail": "Text can not be empty",
                "error_code": "text_cannot_be_empty",
            },
        )

    try:
        text_completion = TextCompletionLLM()
        stream = text_completion.stream_response(text)
        return StreamingResponse(stream, media_type="text/event-stream")
    except Exception as e:
        # TODO: add logging
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "detail": str(e),
                "error_code": "internal_server_error",
            },
        )
