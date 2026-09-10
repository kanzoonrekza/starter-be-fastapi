"""Request/response shapes. What goes over the wire, not what goes in the DB."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
