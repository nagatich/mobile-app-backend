from rest_framework import serializers

from mercedes.serializers import DynamicFieldsModelSerializer
from .models import WishListItem

class WishListItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WishListItem
        exclude = [
            'user'
        ]
