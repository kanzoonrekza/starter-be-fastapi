FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev
COPY . .
ENV PATH=/app/.venv/bin:$PATH PORT=8000
EXPOSE 8000
CMD ["sh", "-c", "fastapi run app/main.py --port $PORT"]
