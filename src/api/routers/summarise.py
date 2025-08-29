from typing import Union

from fastapi import APIRouter, status, Request
from fastapi.responses import StreamingResponse, JSONResponse

from src.api.schemas import SummariseRequest, error_responses
from src.core.limiter import get_limiter
from src.core.services.llm import SummariseLLM
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1", tags=["Summarise"])

limiter = get_limiter()


# Response Models
class SummarySuccessResponse(BaseModel):
    """Successful streaming response model"""

    content: str
    media_type: str = "text/plain"


@router.post(
    "/summarise",
    response_class=StreamingResponse,
    responses={
        **error_responses,
        200: {
            "content": {"text/event-stream": {}},
            "description": "Successful streaming response",
        },
    },
    response_model=SummarySuccessResponse,  # For documentation purposes
    summary="Stream text summarisation",
    description="Streams summarised text in real-time using LLMs",
)
@limiter.limit("20/minute")
async def summarise(
    request: Request,
    request_obj: SummariseRequest,
) -> Union[StreamingResponse, JSONResponse]:
    """
    Summarises input text using a Language Model (LLM) and streams
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
        summarizer = SummariseLLM()
        stream = summarizer.stream_response(text)
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
