import json

from mercedes.celery import app

from parser.drom import Drom

from core.models import (
    Brand,
    Model,
    Generation,
)

@app.task
def update_generations():
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
    except Exception as e:
        print(e)
