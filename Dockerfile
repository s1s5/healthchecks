FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py ./
COPY hc ./hc
COPY locale ./locale
COPY static ./static
COPY stuff ./stuff
COPY templates ./templates
COPY wait-for-it.sh ./wait-for-it.sh
COPY healthcheck-app.py ./healthcheck-app.py
COPY CHANGELOG.md ./CHANGELOG.md

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
