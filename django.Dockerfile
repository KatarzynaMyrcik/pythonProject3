FROM python:3.8

WORKDIR app

RUN pip install DJango gunicorn psycopg2

COPY mysite .

CMD gunicorn --bind=0.0.0.0:8000 mysite.wsgi
