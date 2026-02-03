"""
ASGI config for music_legends project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_legends.settings')

application = get_asgi_application()
