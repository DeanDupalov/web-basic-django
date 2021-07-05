from django.contrib.auth.forms import UserCreationForm

from core.bootstrap_form import BootstrapFormMixin


class SignupForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()
