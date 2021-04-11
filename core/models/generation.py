from django.db import models

from .model import Model

class Generation(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    family = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    production_period = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.model.brand.name} - {self.model.name} - {self.name}'
