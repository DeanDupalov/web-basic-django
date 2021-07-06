from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import UserProfile


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown'),
    )

    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=6)
    age = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='pets_images')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, Type: {self.type}, Age: {self.age}'

    class Meta:
        verbose_name_plural = 'pets'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # test = models.CharField(max_length=3, default='foo')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

