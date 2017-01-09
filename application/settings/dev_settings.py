# -*- coding: utf-8 -*-

import os

from settings.base_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
AUTO_LOGIN = DEBUG

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(ROOT_PATH, '../../static')
MEDIA_URL = '/static'
MEDIA_CSS = '/static/css'
MEDIA_JS = '/static/js'
MEDIA_IMG = '/static/img'
MEDIA_USER_BK_IMG = '/static/user'
