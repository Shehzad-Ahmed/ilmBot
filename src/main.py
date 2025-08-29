from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from src.api.routers import health_check, summarise, text_completion

from slowapi.errors import RateLimitExceeded

from src.core.limiter import get_limiter

app = FastAPI()

app.state.limiter = get_limiter()


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc), "error_code": "internal_server_error"},
    )


@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests", "error_code": "rate_limit_exceeded"},
    )


app.include_router(health_check.router)
app.include_router(summarise.router)
app.include_router(text_completion.router)
