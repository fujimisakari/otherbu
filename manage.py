#!/usr/bin/env python

import os
import sys
import dotenv

if __name__ == '__main__':

    if os.environ.get('APP_ENV') and os.environ['APP_ENV'] == 'production':
        dotenv.load_dotenv('.env_production')
    else:
        dotenv.load_dotenv('.env_develop')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
