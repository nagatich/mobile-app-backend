import json

from channels.db import database_sync_to_async

from mercedes.consumers import Consumer

from ..models import Modification, Model, Generation
from ..serializers import ModificationSerializer
from ..events import MODIFICATION_LIST

class ModificationListConsumer(Consumer):
    model = Modification
    serializer_class = ModificationSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(event=MODIFICATION_LIST, *args, **kwargs)

    async def connect(self):
        await super().connect()
        await self.send()

    async def receive(self, text_data):
        data = json.loads(text_data)
        brands = await self.get_modification_list(data)
        await self.channel_layer.group_send(
            self.room,
            {
                'type': 'notificate',
                'event': MODIFICATION_LIST,
                'message': brands
            }
        )

    async def send(self):
        qs = self.scope['query_string_params']
        brands = await self.get_modification_list(qs)
        await self.channel_layer.group_send(
            self.room,
            {
                'type': 'notificate',
                'event': MODIFICATION_LIST,
                'message': brands,
            }
        )

    @database_sync_to_async
    def get_modification_list(self, data):
        try:
            brand_name = data.get('brand_name')
            model_name = data.get('model_name')
            number = data.get('generation')
            model = Model.objects.get(
                brand__name__iexact=brand_name,
                name__iexact=model_name
            )
            generation = Generation.objects.get(model=model, number=number)
            generations = self.model.objects.filter(generation=generation)
            serializer = self.serializer_class(instance=generations, many=True)
            return serializer.data
        except:
            return []

