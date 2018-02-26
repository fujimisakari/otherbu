# Nginx Dockerfile

FROM debian:jessie

ENV TZ Asia/Tokyo

RUN apt-get update \
    && apt-get install -y wget \
    && wget http://nginx.org/packages/keys/nginx_signing.key \
    && cat nginx_signing.key | apt-key add - \
    && echo "deb http://httpredir.debian.org/debian/ jessie-backports main contrib non-free" >> /etc/apt/sources.list \
    && echo "deb-src http://httpredir.debian.org/debian/ jessie-backports main contrib non-free" >> /etc/apt/sources.list \
    && echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list \
    && echo "deb-src http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -t jessie-backports -y openssl \
    && apt-get install -y gettext-base nginx \
    && rm -rf /var/lib/apt/lists/*

RUN rm /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
