import os
import sys

IS_MAINTENANCE = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG
AUTO_LOGIN = DEBUG

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
APP_PATH = os.path.join(CURRENT_PATH, '../')
sys.path.append(APP_PATH)

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

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ROOT_URLCONF = 'web.urls'

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'module.misc.middleware.TemplateFilterMiddleware',
    'module.misc.middleware.ExceptionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # module
    'module.setting',
    'module.oauth',
    'module.misc',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'web.context_processors.common_context',
                'web.context_processors.user_context',
            ],
            'debug': True,
        },
    },
]

PC_TEMPLATE_DIRS = [
    os.path.join(APP_PATH, 'templates/pc'),
]

SMARTPHONE_TEMPLATE_DIRS = [
    os.path.join(APP_PATH, 'templates/sp'),
]

# Static settting
STATIC_URL = os.environ.get('STATIC_URL')
STATICFILES_DIRS = (
    [os.path.join(APP_PATH, '../static')]
)

# Media setting
MEDIA_URL = os.environ.get('MEDIA_URL')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ.get('MEMCACHED_LOCATION'),
        'TIMEOUT': 3600 * 24,  # 24h
    },
}

LOGGING_DIR = '/tmp'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },

        'file_rotate': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGGING_DIR + '/app.log',
            'maxBytes': 1024 * 1024 * 5 * 10,  # 50MB
            'backupCount': 10,
            'formatter': 'standard'
        },

    },
    'loggers': {
        'django.request': {
            'handlers': ['file_rotate'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# 別ホストからのリレーションを許可する
ALLOWED_HOSTS = ['*']

# S3
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
S3_ACCESS_KEY_ID = os.environ.get('S3_ACCESS_KEY_ID')
S3_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET_ACCESS_KEY')


#####################################################################

# System
PASSPORT_EXPIRE = 30         # 自動ログインの期限(30日)
UPLOAD_SIZE_LIMIT = 2097152  # byte単位(2M = 2097152byte)

# OAuth_key
# twiiter
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

# facebook
FACEBOOK_APP_KEY = os.environ.get('FACEBOOK_APP_KEY')
FACEBOOK_APP_SECRET = os.environ.get('FACEBOOK_APP_SECRET')
FACEBOOK_REDIRECT_URI = os.environ.get('FACEBOOK_REDIRECT_URI')

# DEMO
DEMO_USER_ID = os.environ.get('DEMO_USER_ID')
DEMO_RESET_TIME = 10

# Conmmon
SITE_TITLE = 'OtherBu'
USER_IMG_DIR = 'media/user'
USER_TMP_DIR = os.path.join(APP_PATH, '../media/user/tmp')
SAMPLE_IMG_PATH = os.path.join(APP_PATH, '../master_data/debug.user/bk_image.jpg')
BK_IMAGE_NAME = "bk_image"     # 背景画像名
USER_IMAGE = "user_image.jpg"  # ユーザー画像

# Root
ROOT_TITLE = 'OtherBu'

# Portal
PORTAL_TITLE = 'OtherBu'
COLUMN = [1, 2, 3]

# Setting
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

# Design
LINKMARK_FLG = 0
LINK_COLOR = "#444444"
CATEGORY_BACK_COLOR = "#ffe599"
PORTAL_BACK_KIND = 1
PORTAL_BACK_COLOR = "#ffffff"
IMAGE_POSITION = "no-repeat"
BK_IMAGE_EXT = "jpg"

# Bookmark, Category
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
