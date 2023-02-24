from django.urls import path

from channels.routing import URLRouter

from notifications.consumers import NotificationConsumer
from core.routing import websocket_urlpatterns as core
from wish_list.routing import websocket_urlpatterns as wish_list

websocket_urlpatterns = URLRouter([
    path('ws/notifications/', NotificationConsumer.as_asgi()),
    path('ws/', core),
    path('ws/wish_list/', wish_list),
])
