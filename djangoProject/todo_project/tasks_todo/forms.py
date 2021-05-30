from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator

from tasks_todo.validators import checkStartsWithUpperCase, check_age


class ProfileForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(6),
            checkStartsWithUpperCase,
        ]
    )
    age = forms.IntegerField(
        label='Your name',
        widget=forms.NumberInput,
        validators=[
            check_age,
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput,



    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            MinLengthValidator(8)
        ]

    )
    text = forms.CharField(
        widget=forms.Textarea
    )
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError('This is a bot!')