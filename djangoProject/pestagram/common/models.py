from django.db import models

from accounts.models import UserProfile
from pets.models import Pet


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(max_length=100, default='')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

