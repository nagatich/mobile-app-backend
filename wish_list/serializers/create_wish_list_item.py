from mercedes.serializers import DynamicFieldsModelSerializer
from wish_list.models import WishListItem

class CreateWishListItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WishListItem
        exclude = [
            'user'
        ]
