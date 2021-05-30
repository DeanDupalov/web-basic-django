from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.name
