"""Tables. Every model lives here so Alembic autogenerate sees all of them."""

from app.db import (
    Base,  # noqa: F401  -- re-exported so models can `from app.models import Base`
)
