import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mercedes.settings')
django_asgi_app = get_asgi_application()

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from notifications.consumers import NotificationConsumer
from notifications.middleware import AuthMiddleware

websocket_urlpatterns = [
    path('ws/notifications/', NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddleware(
        URLRouter(
            websocket_urlpatterns,
        )
    ),
})
