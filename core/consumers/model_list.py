from channels.db import database_sync_to_async

from mercedes.consumers import Consumer

from ..models import Model
from ..serializers import ModelSerializer
from ..events import MODEL_LIST

class ModelListConsumer(Consumer):
    model = Model
    serializer_class = ModelSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(event=MODEL_LIST, *args, **kwargs)

    async def connect(self):
        await super().connect()
        await self.send()

    async def send(self):
        models = await self.get_model_list()
        await self.channel_layer.group_send(
            self.room,
            {
                'type': 'notificate',
                'event': MODEL_LIST,
                'message': models,
            }
        )

    @database_sync_to_async
    def get_model_list(self):
        try:
            qs = self.scope['query_string_params']
            brand_name = qs.get('brand_name')
            generations = self.model.objects.filter(brand__name__iexact=brand_name)
            serializer = self.serializer_class(instance=generations, many=True)
            return serializer.data
        except:
            return []
