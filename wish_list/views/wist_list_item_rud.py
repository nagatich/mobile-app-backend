from rest_framework import generics

from mercedes.permissions import IsOwner

from wish_list.models import WishListItem
from wish_list.serializers import WishListItemSerializer

class WishListRUDView(generics.RetrieveUpdateDestroyAPIView):
    model = WishListItem
    serializer_class = WishListItemSerializer
    permission_classes=[IsOwner]

    def get_queryset(self):
        return self.model.objects.all()

