from django.urls import path

from .views import *

urlpatterns = [
    path('', home),
    path('get_cars_list/', CarListAPIView.as_view()),
    path('get_cars_models/<str:car_name>/', CarModelListAPIView.as_view()),
    path('get_model_generations/<str:model_name>/', ModelGenerationListAPIView.as_view()),
    path('get_generation_modifications/<str:model_name>/<str:generation>/', GenerationModificationListAPIView.as_view()),
    path('query', QueryAPIView.as_view()),
]
