from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):  # Create your models here.
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(1)
        ]
    )
    image = models.ImageField(upload_to='profile')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='expenses')
    description = models.TextField()
    price = models.FloatField(
        validators=[
            MinValueValidator(0),
        ]
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
