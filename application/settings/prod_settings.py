# -*- coding: utf-8 -*-

from settings.base_settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
AUTO_LOGIN = DEBUG

STATIC_URL = 'https://s3-ap-northeast-1.amazonaws.com/static-otherbu-prod/'
MEDIA_URL = '/media/'
