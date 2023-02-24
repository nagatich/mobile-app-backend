from django.urls import path

from channels.routing import URLRouter

from .consumers import WishListConsumer

websocket_urlpatterns = URLRouter([
    path('', WishListConsumer.as_asgi()),
])
