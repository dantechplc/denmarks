"""
WSGI config for denmark project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from decouple import config
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'denmark.settings_pro' if config(
        'DJANGO_ENVIRONMENT') == 'production' else 'denmark.settings_dev')

application = get_wsgi_application()
