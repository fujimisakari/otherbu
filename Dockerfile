FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV WERKZEUG_DEBUG_PIN off
ENV DOCKER true

RUN apt-get update
RUN apt-get install -y mysql-client vim net-tools telnet curl
RUN pip install --no-cache-dir -r env/requirements.txt
