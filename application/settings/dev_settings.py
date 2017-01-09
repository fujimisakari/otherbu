# -*- coding: utf-8 -*-

import os
import socket

from settings.base_settings import *

HOSTNAME = socket.gethostname()

# 本番サーバーのdevではoauth認証を行うようにする
if HOSTNAME == PUBLIC_HOSTNAME:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    AUTO_LOGIN = False
else:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    AUTO_LOGIN = DEBUG

# 本番環境以外ではmemcachedは使用しない
CACHES = {}


# ==================================================
#  OAuth認証キー(dev環境用)
# ==================================================

# twiiter
TWITTER_CONSUMER_KEY = DEV_MY_TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = DEV_MY_TWITTER_CONSUMER_SECRET

# facebook
FACEBOOK_APP_KEY = DEV_MY_FACEBOOK_APP_KEY
FACEBOOK_APP_SECRET = DEV_MY_FACEBOOK_APP_SECRET
FACEBOOK_REDIRECT_URI = DEV_MY_FACEBOOK_REDIRECT_URI


# ==================================================
#  DB設定(本番サーバー内でのdev環境用)
# ==================================================

if HOSTNAME == PUBLIC_HOSTNAME:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': DEV_DB_NAME,
            'USER': DEV_DB_USER,
            'PASSWORD': DEV_DB_PASS,
            'HOST': '',
            'PORT': '',
        }
    }


# ==================================================
#  media設定
# ==================================================

if HOSTNAME != PUBLIC_HOSTNAME:
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    MEDIA_ROOT = os.path.join(ROOT_PATH, '../../static')
    MEDIA_URL = '/static'

    MEDIA_CSS = '/static/css'
    MEDIA_JS = '/static/js'
    MEDIA_IMG = '/static/img'
    MEDIA_USER_BK_IMG = '/static/user'
