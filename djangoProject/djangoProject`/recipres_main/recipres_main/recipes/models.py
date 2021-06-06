from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField(default='')
    ingredients = models.CharField(max_length=250)
    time = models.IntegerField(default=0)

    def __str__(self):
        return f'ID: {self.id}, Title: {self.title}'
