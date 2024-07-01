FROM python:3.12.0
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$PATH:/root/.local/bin/
COPY . /app
WORKDIR /app
RUN poetry install
ENTRYPOINT poetry run flask run --host 0.0.0.0
#commit first working dockerfile