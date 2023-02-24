from channels.db import database_sync_to_async

from mercedes.consumers import Consumer

from ..models import Generation, Model
from ..serializers import GenerationSerializer
from ..events import GENERATION_LIST

class GenerationListConsumer(Consumer):
    model = Generation
    serializer_class = GenerationSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(event=GENERATION_LIST, *args, **kwargs)

    async def connect(self):
        await super().connect()
        await self.send()

    async def send(self):
        generations = await self.get_generation_list()
        await self.channel_layer.group_send(
            self.room,
            {
                'type': 'notificate',
                'event': GENERATION_LIST,
                'message': generations,
            }
        )

    @database_sync_to_async
    def get_generation_list(self):
        try:
            qs = self.scope['query_string_params']
            brand_name = qs.get('brand_name')
            model_name = qs.get('model_name')
            model = Model.objects.get(
                brand__name__iexact=brand_name,
                name__iexact=model_name
            )
            generations = self.model.objects.filter(model=model)
            serializer = self.serializer_class(instance=generations, many=True)
            return serializer.data
        except:
            return []
