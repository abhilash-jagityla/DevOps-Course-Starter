FROM python:3.12.0
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY . /app
# RUN poetry install
# ENTRYPOINT poetry run flask run
