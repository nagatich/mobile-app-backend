from rest_framework import generics

from user_profile.models import Car
from user_profile.serializers import DetailedCarSerializer

class UserCarsListAPIView(generics.ListAPIView):
    model = Car
    serializer_class = DetailedCarSerializer

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-modification', '-generation', '-model')
