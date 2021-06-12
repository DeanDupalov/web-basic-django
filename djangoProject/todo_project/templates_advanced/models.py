from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}: {self.price}'
