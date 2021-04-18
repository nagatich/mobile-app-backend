from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('auth/', include('custom_auth.urls')),
    path('wish_list/', include('wish_list.urls')),
    path('profile/', include('user_profile.urls')),
]
