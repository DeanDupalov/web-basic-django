from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'title',
            'description',
            'is_done',
        ]


class RawTodoForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    is_done = forms.BooleanField()


