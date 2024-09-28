"""
ASGI config for chegg project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
#ASGI(Asynchronous Server Gateway Interface) acts as a specification that allows Django and other frameworks to support asynchronous, real-time operations such as WebSockets.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chegg.settings')

application = get_asgi_application()
