from django import forms
from django.core.exceptions import ValidationError

from core.utiles import get_profile
from expenses_tracker.app.models import Expense, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

    def clean_price(self):
        profile = get_profile()
        price = float(self.cleaned_data['price'])
        if profile.budget_left < price:
            raise ValidationError('Not enough budget!')
        return price

class DisabledFormMixin:
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class DeleteExpenseForm(ExpenseForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
