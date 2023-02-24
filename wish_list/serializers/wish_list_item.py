from mercedes.serializers import DynamicFieldsModelSerializer
from wish_list.models import WishListItem

from core.serializers import (
    BrandSerializer,
    ModelSerializer,
    GenerationSerializer,
    ModificationSerializer,
)

class WishListItemSerializer(DynamicFieldsModelSerializer):
    brand = BrandSerializer()
    model = ModelSerializer()
    generation = GenerationSerializer()
    modification = ModificationSerializer()

    class Meta:
        model = WishListItem
        exclude = [
            'user'
        ]
