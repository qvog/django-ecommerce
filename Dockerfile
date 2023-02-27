FROM python:3.8-slim

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV STATIC_ROOT /var/lib/django-static

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev locales-all && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uwsgi==2.0.19
ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt    

WORKDIR /srv

COPY . /srv

ENV NO_CACHE=On
RUN ./manage.py collectstatic --noinput
ENV NO_CACHE=Off

USER nobody

CMD ["gunicorn", "-b", "0.0.0.0:8001","vivasonya.wsgi:application"]
