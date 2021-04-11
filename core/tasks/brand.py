import json

from mercedes.celery import app

from parser.drom import Drom

from core.models import Brand

@app.task
def update_brands():
    try:
        cars = Drom().get_car_list()
        for car in cars.get('items'):
            brand, created = Brand.objects.get_or_create(name=car.get('name'))
    except Exception as e:
        print(e)
