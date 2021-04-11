from django.db import models

from .brand import Brand

class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand.name} - {self.name}'
