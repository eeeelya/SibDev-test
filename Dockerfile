FROM python:3.10-alpine

COPY ./sibdev /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="."

RUN pip install pipenv \
    && pipenv install --system --ignore-pipfile --dev

ENTRYPOINT ["/app/entrypoint.sh"]
