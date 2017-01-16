FROM python:2.7

ENV TZ Asia/Tokyo
ENV PYTHONDONTWRITEBYTECODE 1
ENV WERKZEUG_DEBUG_PIN off
ENV DOCKER true

RUN mkdir /usr/src/otherbu_dev
RUN mkdir /usr/src/otherbu_stating
RUN mkdir /usr/src/otherbu_prod

RUN mkdir /var/run/otherbu_dev
RUN mkdir /var/run/otherbu_staging
RUN mkdir /var/run/otherbu_prod

RUN apt-get update
RUN apt-get install -y mysql-client vim net-tools telnet curl
ADD env/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
