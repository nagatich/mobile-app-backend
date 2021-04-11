import json

from mercedes.celery import app

from parser.drom import Drom

from core.models import (
    Brand,
    Model,
)

@app.task
def update_models():
    try:
        brands = Brand.objects.all()
        for brand in brands:
            models = Drom().get_car_models(brand.name)
            for model in models.get('items'):
                m, created = Model.objects.get_or_create(name=model.get('name'), brand=brand)
    except Exception as e:
        print(e)
