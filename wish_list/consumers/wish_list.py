from channels.db import database_sync_to_async

from mercedes.consumers import Consumer

from ..models import WishListItem
from ..serializers import CreateWishListItemSerializer
from ..events import WISH_LIST

class WishListConsumer(Consumer):
    model = WishListItem
    serializer_class = CreateWishListItemSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(room=WISH_LIST, private=True, *args, **kwargs)

    async def send(self):
        wish_list = await self.get_wish_list()
        await self.channel_layer.group_send(
            self.room,
            {
                'type': 'notificate',
                'event': WISH_LIST,
                'message': wish_list,
            }
        )

    @database_sync_to_async
    def get_wish_list(self):
        wish_list = self.model.objects.filter(user=self.user).order_by('-created')
        serializer = self.serializer_class(instance=wish_list, many=True)
        return serializer.data

