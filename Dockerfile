FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV STATIC_ROOT /opt/static

COPY manage.py ./
COPY hc ./hc
# COPY locale ./locale
COPY static ./static
COPY stuff ./stuff
COPY templates ./templates
COPY wait-for-it.sh ./wait-for-it.sh
COPY healthcheck-app.py ./healthcheck-app.py
COPY CHANGELOG.md ./CHANGELOG.md

RUN python manage.py collectstatic
RUN python manage.py compress

CMD ["gunicorn", "hc.wsgi:application", "-b", "0.0.0.0:8000", "--workers", "1", "--threads", "4", "-t", "300", "--log-level", "info"]
