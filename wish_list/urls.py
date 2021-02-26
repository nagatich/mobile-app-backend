from django.urls import path

from .views import *

urlpatterns = [
    path('', WishListItemView.as_view()),
    path('<int:pk>/', WishListRUDView.as_view()),
]
