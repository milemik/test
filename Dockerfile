FROM python:3.8

ENV PYTHONUNBUFFERD 1

EXPOSE 8000

RUN apt-get update -qqy && apt-get upgrade -qqy && apt-get install -qqy \
python-dev python3-distutils build-essential git \
musl-dev libffi-dev libxml2-dev libxslt-dev libjpeg-dev zlib1g-dev gettext graphviz-dev git

COPY wait-for-it.sh /usr/bin/

RUN chmod 755 /usr/bin/wait-for-it.sh

RUN pip install --upgrade pip pipenv

WORKDIR /tmp

COPY Pipfile Pipfile.lock /tmp/

RUN pipenv install --dev --skip-lock --system

COPY . /app

WORKDIR /app

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]