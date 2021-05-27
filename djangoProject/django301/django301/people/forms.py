from django import forms


class RawPersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    home_town = forms.CharField(max_length=100)