from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
)

from wish_list.models import WishListItem
from wish_list.serializers import WishListItemSerializer

class WishListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    model = WishListItem
    serializer_class = WishListItemSerializer

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

