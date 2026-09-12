# AGENTS.md

FastAPI + SQLAlchemy 2.0 + Alembic starter. Managed by `uv`, Python >= 3.14.

## Commands

All via `make` (it `-include`s `.env` and exports it, so env vars are loaded for every target — don't run bare `uv run` if the command needs `.env`):

- `make install` — `uv sync`
- `make dev` / `make run` — dev server / prod server on `$PORT` (default 8000)
- `make migration m="message"` — alembic autogenerate revision
- `make migrate` / `make rollback` — upgrade head / downgrade -1

No test, lint, or typecheck setup exists yet. Don't invent commands; if you add tooling, add a Makefile target for it.

## Layout rules (enforced by module docstrings — read them before editing)

- `app/main.py` — assembly only: build app, include routers. **No endpoints here.**
- `app/config.py` — every env var the app reads is a `Settings` field. Nowhere else reads `os.environ`. Add new vars here *and* to `.env.example`.
- `app/db.py` — engine, `Base`, `get_db` session dependency. Nothing else.
- `app/models.py` — all tables live in this one file so Alembic autogenerate sees them. Re-exports `Base`.
- `app/schemas.py` — pydantic wire shapes, separate from ORM models.
- `app/routers/<name>.py` — one `router = APIRouter(tags=[...])` per file, registered in `main.py`.

## Gotchas

- `migrations/env.py` sets the DB URL from `app.config.settings`, not `alembic.ini`. Never put a URL in `alembic.ini`.
- `migrations/env.py` imports `app.models` for side effects; a model not reachable from `app/models.py` will be silently omitted from autogenerate.
- `pydantic-settings` is used by `app/config.py` but is only present transitively via `fastapi[standard-no-fastapi-cloud-cli]`. If that extra changes, add it to `pyproject.toml` explicitly.
- `migrations/versions/` is empty — there is no baseline migration yet.
- `.env` is gitignored; `.env.example` is the contract. `PORT` is read by the Makefile only, the rest by `app/config.py`.
