import json

from django.contrib.auth.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from mercedes.celery import app

from parser.drom import Drom

from core.models import (
    Brand,
    Model,
    Generation,
)

from notifications.models import Notification

@app.task
def update_generations(user_id):
    user = User.objects.get(id=user_id)
    try:
        brands = Brand.objects.all()
        for brand in brands:
            models = Model.objects.filter(brand=brand)
            for model in models:
                model_name = f'{brand.name} {model.name}'
                generations = Drom().get_model_generations(model_name)
                for generation in generations.get('items'):
                    g, created = Generation.objects.get_or_create(
                        model=model,
                        name=generation.get('name'),
                        family=json.dumps(generation.get('family')),
                        number=generation.get('number'),
                        production_period=json.dumps(generation.get('productionPeriod'))
                    )
        Notification.objects.create(
            to_user=user,
            message='Обновление поколений завершено!',
            event='update_success',
        )
    except Exception as e:
        print(e)
        Notification.objects.create(
            to_user=user,
            message='При обновлении поколений что-то пошло не так!',
            event='update_error',
        )
