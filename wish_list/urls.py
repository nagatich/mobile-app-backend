from django.urls import path

from .views import *

urlpatterns = [
    path('', WishListAPIView.as_view()),
    path('<int:pk>/', WishListRUDView.as_view()),
]
