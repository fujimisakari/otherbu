import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

paths = ('../application',)
current_path = os.path.dirname(__file__)
for path in paths:
    sys.path.insert(0, os.path.abspath(os.path.join(current_path, path)))

application = get_wsgi_application()
