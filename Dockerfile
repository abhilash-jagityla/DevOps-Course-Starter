FROM python:3.12.0 AS base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/
WORKDIR /app
COPY pyproject.toml poetry.toml /app/
RUN /root/.local/bin/poetry install
COPY todo_app /app/todo_app

FROM base as production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as test
COPY .env.test /app/
ENTRYPOINT poetry run pytest
