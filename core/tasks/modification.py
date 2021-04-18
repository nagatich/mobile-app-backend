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
    Modification,
)
from notifications.models import Notification
from notifications.events import (
    UPDATE_DB_ERROR,
    UPDATE_DB_SUCCESS
)

@app.task
def update_modifications(user_id):
    user = User.objects.get(id=user_id)
    try:
        brands = Brand.objects.all()
        for brand in brands:
            models = Model.objects.filter(brand=brand)
            for model in models:
                generations = Generation.objects.filter(model=model)
                for generation in generations:
                    model_name = f'{brand.name} {model.name}'
                    modifications = Drom().get_generation_modifications(model_name, generation.number)
                    for modification in modifications.get('items'):
                        m, created = Modification.objects.get_or_create(
                            name=modification.get('name'),
                            generation=generation,
                            fuel=modification.get('fuel'),
                            volume=modification.get('volume'),
                            power_range=json.dumps(modification.get('powerRange'))
                        )
        if user_id:
            Notification.objects.create(
                to_user=user,
                message='Обновление модификаций завершено!',
                event=UPDATE_DB_SUCCESS,
            )
    except Exception as e:
        print(e)
        if user_id:
            Notification.objects.create(
                to_user=user,
                message='При обновлении модификаций что-то пошло не так!',
                event=UPDATE_DB_ERROR,
            )
