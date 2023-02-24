from channels.db import database_sync_to_async

from mercedes.consumers import Consumer

from ..models import Brand
from ..serializers import BrandSerializer
from ..events import BRAND_LIST

class BrandListConsumer(Consumer):
    model = Brand
    serializer_class = BrandSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(room=BRAND_LIST, *args, **kwargs)
    
    async def connect(self):
        await super().connect()
        await self.send()

    async def send(self):
        brands = await self.get_brand_list()
        await self.channel_layer.group_send(
            self.room,
            {
                'type': 'notificate',
                'event': BRAND_LIST,
                'message': brands,
            }
        )

    @database_sync_to_async
    def get_brand_list(self):
        brands = self.model.objects.all()
        serializer = self.serializer_class(instance=brands, many=True)
        return serializer.data
