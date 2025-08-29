from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/health-check", tags=["healthcheck"])


@router.get("/")
async def health_check():
    return HTMLResponse("I am alive!")
