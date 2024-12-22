"""
WSGI config for ecommerce_rest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# aca traigo la version loca o de produccion, poer eso elimino el setting.py y creo mi propia carpeta settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_rest.settings.local')

application = get_wsgi_application()
