from django.db import models
from django.contrib.auth.models import User

from core.models import (
    Brand,
    Model,
    Generation,
    Modification,
)

PRIORITY_CHOICES = (
    (0, 'Low'),
    (1, 'Medium'),
    (2, 'High'),
)

class WishListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, blank=True, null=True)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE, blank=True, null=True)
    modification = models.ForeignKey(Modification, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=500)
    min_cost = models.IntegerField(default=0)
    max_cost = models.IntegerField(default=0)
    avg_cost = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)

    def __str__(self):
        return f'{self.name}'

