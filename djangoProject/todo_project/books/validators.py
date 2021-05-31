from django.core.exceptions import ValidationError


def min_pages_count(value):
    if value <= 0:
        raise ValidationError(f'Pages count must be greater than 0. Now is {value}')