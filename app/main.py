"""Assembly only: build the app, attach routers. No endpoints in this file."""

from fastapi import FastAPI

from app.config import settings
from app.routers import health, root

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(root.router)
app.include_router(health.router)
