import os

if os.environ['APP_ENV'] == 'production':
    from .production import *
else:
    from .develop import *
