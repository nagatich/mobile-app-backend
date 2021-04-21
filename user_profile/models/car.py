from django.db import models
from django.contrib.auth.models import User

from core.models import (
    Brand,
    Model,
    Generation,
    Modification,
)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, blank=True, null=True)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE, blank=True, null=True)
    modification = models.ForeignKey(Modification, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_searched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.brand.name} \
            {self.model.name if self.model else None} \
            {self.generation.name if self.generation else None} \
            {self.modification.name if self.modification else None}'
