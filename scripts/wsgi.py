import os
import sys

import dotenv
from django.core.wsgi import get_wsgi_application

current_path = os.path.dirname(__file__)

if os.environ.get('APP_ENV') and os.environ['APP_ENV'] == 'production':
    dotenv.load_dotenv(os.path.join(current_path, '../.env_production'))
else:
    dotenv.load_dotenv(os.path.join(current_path, '../.env_develop'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

paths = ('../application',)
for path in paths:
    sys.path.insert(0, os.path.abspath(os.path.join(current_path, path)))

application = get_wsgi_application()
