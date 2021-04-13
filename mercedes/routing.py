# from django.urls import path

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter

# from notifications.consumers import NotificationConsumer

# websockets = URLRouter([
#     path(
#         "notifications/",
#         NotificationConsumer,
#         name="ws_notifications",
#     ),
# ])

# application = ProtocolTypeRouter({
#     "websocket": AuthMiddlewareStack(websockets),
# })

from django.urls import path

from notifications.consumers import NotificationConsumer

websocket_urlpatterns = [
    path('notifications/', NotificationConsumer.as_asgi()),
]
