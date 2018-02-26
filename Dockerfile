FROM python:3.6.4

ENV TZ Asia/Tokyo

RUN mkdir /usr/src/otherbu
RUN mkdir /var/run/otherbu

WORKDIR /usr/src/otherbu

RUN apt-get update
RUN apt-get install -y mysql-client vim net-tools telnet curl

ADD . /usr/src/otherbu
RUN pip install --no-cache-dir -r requirements.txt
