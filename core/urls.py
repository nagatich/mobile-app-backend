from django.urls import path

from .views import *
from .tasks import (
    update_brands,
    update_models,
    update_generations,
    update_modifications,
)

urlpatterns = [
    path('', home),
    
    path('update_brands/', UpdateAPIView.as_view(update_function=update_brands)),
    path('update_models/', UpdateAPIView.as_view(update_function=update_models)),
    path('update_generations/', UpdateAPIView.as_view(update_function=update_generations)),
    path('update_modifications/', UpdateAPIView.as_view(update_function=update_modifications)),

    path('get_brand_list/', BrandListAPIView.as_view()),
    path('get_model_list/<str:brand_name>/', ModelListAPIView.as_view()),
    path('get_generation_list/<str:brand_name>/<str:model_name>/', GenerationListAPIView.as_view()),
    path('get_modification_list/<str:brand_name>/<str:model_name>/<str:generation>/', ModificationListAPIView.as_view()),
    path('query', QueryAPIView.as_view()),
]
