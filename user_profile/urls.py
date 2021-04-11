from django.urls import path

from .views import *

urlpatterns = [
    path('cars/', UserCarsListAPIView.as_view()),
]
