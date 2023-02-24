from django.urls import path

from channels.routing import URLRouter

from core.consumers import BrandListConsumer, GenerationListConsumer, ModelListConsumer, ModificationListConsumer

websocket_urlpatterns = URLRouter([
    path('brand_list/', BrandListConsumer.as_asgi()),
    path('model_list/', ModelListConsumer.as_asgi()),
    path('generation_list/', GenerationListConsumer.as_asgi()),
    path('modification_list/', ModificationListConsumer.as_asgi()),
])
