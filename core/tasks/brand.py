import json

from django.contrib.auth.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from mercedes.celery import app
from parser.drom import Drom
from core.models import Brand
from notifications.models import Notification
from notifications.events import (
    UPDATE_DB_ERROR,
    UPDATE_DB_SUCCESS
)

@app.task
def update_brands(user_id=None):
    if user_id:
        user = User.objects.get(id=user_id)
    try:
        cars = Drom().get_car_list()
        for car in cars.get('items'):
            brand, created = Brand.objects.get_or_create(name=car.get('name'))
        if user_id:
            Notification.objects.create(
                to_user=user,
                message='Обновление брендов завершено!',
                event=UPDATE_DB_SUCCESS,
            )
    except Exception as e:
        print(e)
        if user_id:
            Notification.objects.create(
                to_user=user,
                message='При обновлении брендов что-то пошло не так!',
                event=UPDATE_DB_ERROR,
            )
