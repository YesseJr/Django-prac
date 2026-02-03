"""
WSGI config for music_legends project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_legends.settings')

application = get_wsgi_application()
