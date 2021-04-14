"""
ASGI config for mercedes project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mercedes.settings")
django_asgi_app = get_asgi_application()

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from notifications.consumers import NotificationConsumer
from notifications.middleware import AuthMiddleware

websocket_urlpatterns = [
    path('notifications/', NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddleware(
        URLRouter(
            websocket_urlpatterns,
        )
    ),
})
