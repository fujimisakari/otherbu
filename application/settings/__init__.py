# -*- coding: utf-8 -*-

import os

if os.environ.get('APP_ENV') == 'local' or os.environ.get('APP_ENV') == 'dev':
    from settings.dev_settings import *
elif os.environ.get('APP_ENV') == 'staging':
    from settings.staging_settings import *
elif os.environ.get('APP_ENV') == 'production':
    from settings.base_settings import *
