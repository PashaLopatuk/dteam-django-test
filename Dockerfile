FROM python:3.13-slim

RUN mkdir /app

WORKDIR /app


# prevent python from creating pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# prevent python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1
# poetry config
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_VIRTUALENVS_PATH=/app/bff_reader/.venv


COPY . /app

RUN chmod +x deploy/worker-entry.sh

RUN apt update
RUN apt install libpq-dev postgresql postgresql-contrib -y

RUN pip install poetr

RUN poetry install --no-root

EXPOSE 8000


RUN cd CVProject

CMD poetry run python CVProject/manage.py runserver 0.0.0.0:8000
