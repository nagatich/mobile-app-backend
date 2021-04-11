from rest_framework import generics

from core.models import Model
from core.serializers import ModelSerializer

class ModelListAPIView(generics.ListAPIView):
    model = Model
    serializer_class = ModelSerializer

    def get_queryset(self):
        try:
            brand_name = self.kwargs.get('brand_name')
            return self.model.objects.filter(brand__name__iexact=brand_name)
        except:
            return None
