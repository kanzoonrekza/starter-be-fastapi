"""Copy this file to start a new router, then wire it in app/main.py."""

from fastapi import APIRouter

from app.schemas import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> HealthResponse:
    return HealthResponse(status="ok")
