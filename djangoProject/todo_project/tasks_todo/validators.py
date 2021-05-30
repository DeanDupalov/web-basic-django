from django.forms import forms


def checkStartsWithUpperCase(value):
    if not value[0].isupper():
        raise forms.ValidationError("Name needs to start with uppercase letter")


def check_age(value):
    if value < 0:
        raise forms.ValidationError("The age cannot be less than zero.")


