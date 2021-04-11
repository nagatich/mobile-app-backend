import json

from mercedes.celery import app

from parser.drom import Drom

from core.models import (
    Brand,
    Model,
    Generation,
    Modification,
)

@app.task
def update_modifications():
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
    except Exception as e:
        print(e)
