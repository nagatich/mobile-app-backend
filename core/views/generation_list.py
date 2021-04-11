from rest_framework import generics

from core.models import (
    Model,
    Generation,
)
from core.serializers import GenerationSerializer

class GenerationListAPIView(generics.ListAPIView):
    model = Generation
    serializer_class = GenerationSerializer

    def get_queryset(self):
        try:
            brand_name = self.kwargs.get('brand_name')
            model_name = self.kwargs.get('model_name')
            model = Model.objects.get(
                brand__name__iexact=brand_name,
                name__iexact=model_name
            )
            return self.model.objects.filter(model=model)
        except:
            return None
