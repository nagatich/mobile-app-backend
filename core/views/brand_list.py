from rest_framework import generics

from core.models import Brand
from core.serializers import BrandSerializer

class BrandListAPIView(generics.ListAPIView):
    model = Brand
    serializer_class = BrandSerializer

    def get_queryset(self):
        return self.model.objects.all()
