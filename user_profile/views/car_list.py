from rest_framework import generics

from user_profile.models import Car
from user_profile.serializers import DetailedCarSerializer

class UserCarsListAPIView(generics.ListAPIView):
    model = Car
    serializer_class = DetailedCarSerializer

    def get_queryset(self):
        qs = self.model.objects.filter(user=self.request.user).order_by(
            '-modification',
            '-generation',
            '-model',
        )
        filter = {}
        for key, value in self.request.GET.items():
            filter[f'{key}__name__iexact'] = value
        qs = qs.filter(**filter)
        return qs.order_by('-last_searched')
