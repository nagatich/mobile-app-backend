import json

from django.contrib.auth.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from mercedes.celery import app

from parser.drom import Drom

from core.models import (
    Brand,
    Model,
)

from notifications.models import Notification

@app.task
def update_models(user_id):
    user = User.objects.get(id=user_id)
    try:
        brands = Brand.objects.all()
        for brand in brands:
            models = Drom().get_car_models(brand.name)
            for model in models.get('items'):
                m, created = Model.objects.get_or_create(name=model.get('name'), brand=brand)
        Notification.objects.create(
            to_user=user,
            message='Обновление моделей завершено!',
            event='update_success',
        )
    except Exception as e:
        print(e)
        Notification.objects.create(
            to_user=user,
            message='При обновлении моделей что-то пошло не так!',
            event='update_error',
        )
