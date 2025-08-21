FROM python:3.11-slim
ENV POETRY_HOME=/opt/poetry PATH="/opt/poetry/bin:$PATH"
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/* \
 && curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /app
COPY pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi
COPY src ./src
COPY tests ./tests
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
