FROM python:3.10-slim

WORKDIR /dishes

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install Django django-cors-headers django-rest-framework psycopg2-binary

COPY . /dishes

CMD python manage.py runserver 0.0.0.0:8000