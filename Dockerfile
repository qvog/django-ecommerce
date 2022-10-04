FROM python:3.8-slim

VOLUME /var/lib/django-db
ENV DATABASE_URL sqlite:////var/lib/django-db/db.sqlite

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev locales-all

ADD requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /srv
ADD . /srv

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "vivasonya.wsgi:application"]
