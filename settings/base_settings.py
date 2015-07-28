# -*- coding: utf-8 -*-

from settings.private_config import *

IS_MAINTENANCE = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG
AUTO_LOGIN = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# テンプレートで使用
import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# インポートのパスを設定
import sys
sys.path.append(ROOT_PATH + '/module/')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',               # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,               # Or path to database file if using sqlite3.
        'USER': DB_USER,                 # Not used with sqlite3.
        'PASSWORD': DB_PASS,             # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

import socket
HOSTNAME = socket.gethostname()
if HOSTNAME == PUBLIC_HOSTNAME:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT': 3600 * 24,  # 24h
        },
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Tokyo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ja'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = DJANGO_SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'module.misc.middleware.TemplateFilterMiddleware',
    'module.misc.middleware.ExceptionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'hoge.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(ROOT_PATH, '../templates/pc'),
)

# PC版用テンプレート
PC_TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, '../templates/pc'),
)

# スマートフォン版用テンプレート
SMARTPHONE_TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, '../templates/sp'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'south',

    # module
    'module.portal',
    'module.setting',
    'module.oauth',
    'module.client_api',
    'module.misc',

    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # module
    'module.context_processors.common_context',
    'module.context_processors.user_context',
)

#####################################################################

# system
PASSPORT_EXPIRE = 30         # 自動ログインの期限(30日)
UPLOAD_SIZE_LIMIT = 2097152  # byte単位(2M = 2097152byte)

# OAuth_key
# twiiter
TWITTER_CONSUMER_KEY = MY_TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = MY_TWITTER_CONSUMER_SECRET

# facebook
FACEBOOK_APP_KEY = MY_FACEBOOK_APP_KEY
FACEBOOK_APP_SECRET = MY_FACEBOOK_APP_SECRET
FACEBOOK_REDIRECT_URI = MY_FACEBOOK_REDIRECT_URI

# DEMO
DEMO_USER_ID = MY_DEMO_USER_ID
DEMO_RESET_TIME = 10

# conmmon
# MEDIA_BASE = '/media/'
# MEDIA_URL = '/static/'
SITE_TITLE = 'OtherBu'
MEDIA_CSS = '/otherbu/static/css'
MEDIA_JS = '/otherbu/static/js'
MEDIA_IMG = '/otherbu/static/img'
MEDIA_USER_BK_IMG = '/otherbu/static/user'
USER_IMG_DIR = os.path.join(ROOT_PATH, '../static/user')
USER_TMP_DIR = os.path.join(ROOT_PATH, '../static/user/tmp')
SAMPLE_IMG_PATH = os.path.join(ROOT_PATH, '../config/debug.user/bk_image.jpg')
BK_IMAGE_NAME = "bk_image"     # 背景画像名
USER_IMAGE = "user_image.jpg"  # ユーザー画像

# root
ROOT_TITLE = 'OtherBu'

# portal
PORTAL_TITLE = 'OtherBu'
COLUMN = [1, 2, 3]

# setting
CATEGORY_TITLE = 'OtherBu / カテゴリ設定'
BOOKMARK_TITLE = 'OtherBu / ブックマーク設定'
BOOKMARK_MOVE_TITLE = 'OtherBu / ブックマーク移動設定'
PAGE_TITLE = 'OtherBu / ページ設定'
DESIGN_TITLE = 'OtherBu / デザイン設定'
IMPORT_TITLE = 'OtherBu / インポート設定'
EXPORT_TITLE = 'OtherBu / エクスポート設定'
INFO_TITLE = 'OtherBu / OtherBuについて'

# 決め打ちデザイン
# <body>のpadding-topを定義
PORTAL_BODY_PADDING = 60
SETTING_BODY_PADDING = 40

# 初期投入用データ

# design
LINKMARK_FLG = 0
LINK_COLOR = "#444444"
CATEGORY_BACK_COLOR = "#ffe599 "
PORTAL_BACK_KIND = 1
PORTAL_BACK_COLOR = "#ffffff"
IMAGE_POSITION = "no-repeat"
BK_IMAGE_EXT = "jpg"

# bookmark, category
INIT_DATA_LIST = [
    {'category': ('動画サイト', 2, 2, 3, 1),
     'bookmark': [('YouTube - Broadcast Yourself  ', 'http://youtube.co.jp', 1),
                  ('ニコニコ動画(原宿)', 'http://www.nicovideo.jp/video_top/', 2)]},
    {'category': ('SNS', 3, 1, 4, 1),
     'bookmark': [('Facebook - フェイスブック - ログイン (日本語)', 'http://facebook.com', 1),
                  ('Twitter', 'https://twitter.com/', 2, 0),
                  ('ソーシャル・ネットワーキング サービス [mixi(ミクシィ)]', 'http://mixi.jp/', 3)]},
    {'category': ('ポータルサイト', 1, 1, 9, 0),
     'bookmark': [('Google', 'http://google.co.jp', 1),
                 ('Yahoo! JAPAN', 'http://yahoo.co.jp', 2)]},
    {'category': ('お気に入り', 1, 2, 16, 1),
     'bookmark': [('カミソリ・髭剃りとメンズグルーミングの専門店　｜　カミソリ倶楽部', 'http://www.kamisoriclub.co.jp/', 3),
                  ('日本大相撲協会公式サイト', 'http://www.sumo.or.jp/', 2),
                  ('グルメ・レストランガイド 食べログ', 'http://tabelog.com/', 1)]},
]
