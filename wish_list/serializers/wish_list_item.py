from mercedes.serializers import DynamicFieldsModelSerializer
from wish_list.models import WishListItem

class WishListItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WishListItem
        exclude = [
            'user'
        ]
