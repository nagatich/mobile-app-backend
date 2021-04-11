from core.serializers import (
    BrandSerializer,
    ModelSerializer,
    GenerationSerializer,
    ModificationSerializer,
)

from user_profile.serializers import CarSerializer

class DetailedCarSerializer(CarSerializer):
    brand = BrandSerializer()
    model = ModelSerializer(exclude=['brand'])
    generation = GenerationSerializer(exclude=['model'])
    modification = ModificationSerializer(exclude=['generation'])
