from django.core.exceptions import ValidationError
from django.db import models

""" validation function must be in separate file"""
def is_zip_validator(value):
    if not str(value).endswith('.zip'):
        raise ValidationError('Only zip files')



class Pet(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='public/pets')
    passport = models.FileField(
        upload_to='private/documents',
        validators=(
            is_zip_validator,
        )
    )
