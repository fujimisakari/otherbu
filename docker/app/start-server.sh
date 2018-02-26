#!/bin/bash

python manage.py migrate

uwsgi --ini /usr/src/otherbu/scripts/uwsgi.ini
