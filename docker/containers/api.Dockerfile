FROM python:3.10-slim

RUN apt-get update && apt-get install -y gettext

ADD . /Library

ENV PYTHONPATH ''${PYTHONPATH}/Library''
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN chmod +x /Libary/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /Library/docker/scripts/wait-for-it.sh

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /Library/requirements.txt
