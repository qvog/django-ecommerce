FROM python:3.8-slim

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev locales-all && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uwsgi==2.0.19
ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt    

RUN useradd -rms /bin/bash srv && chmod 777 /opt /run

WORKDIR /srv

RUN mkdir /srv/static && mkdir /srv/media && chown -R srv:srv /srv && chmod 755 /srv

ADD . /srv

USER srv

CMD ["gunicorn", "-b", "0.0.0.0:8001","vivasonya.wsgi:application"]
