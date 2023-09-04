FROM python:3.10-alpine

COPY ./sibdev /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="."

RUN pip install pipenv
RUN pipenv install --system --deploy

