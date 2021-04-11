from django.db import models

from .generation import Generation

class Modification(models.Model):
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    fuel = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    volume = models.PositiveIntegerField()
    power_range = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.generation.model.brand.name} - {self.generation.model.name} - {self.generation.name} - {self.name}'
