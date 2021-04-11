from rest_framework import generics

from core.models import (
    Model,
    Generation,
    Modification,
)
from core.serializers import ModificationSerializer

class ModificationListAPIView(generics.ListAPIView):
    model = Modification
    serializer_class = ModificationSerializer

    def get_queryset(self):
        try:
            brand_name = self.kwargs.get('brand_name')
            model_name = self.kwargs.get('model_name')
            number = self.kwargs.get('generation')
            model = Model.objects.get(
                brand__name__iexact=brand_name,
                name__iexact=model_name
            )
            generation = Generation.objects.get(model=model, number=number)
            return self.model.objects.filter(generation=generation)
        except:
            return None
