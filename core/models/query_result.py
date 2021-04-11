from django.db import models
from django.contrib.auth.models import User

from core.models import (
    Brand,
    Model,
    Generation,
    Modification,
)

class QueryResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, blank=True, null=True)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE, blank=True, null=True)
    modification = models.ForeignKey(Modification, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    query = models.CharField(max_length=500)
    minimum = models.FloatField()
    maximum = models.FloatField()
    average = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user}: {self.query}'
