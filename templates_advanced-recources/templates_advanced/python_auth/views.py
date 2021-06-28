from django.contrib.auth import logout, authenticate, login
from django.db import transaction
from django.shortcuts import redirect, render

from python_auth.forms import RegisterForm, ProfileForm


@transaction.atomic
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            login(request, user)

            return redirect('index')

    else:
        form = RegisterForm()
        profile_form = ProfileForm()

    context = {
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'auth/register.html', context)


def login_user(request):
    username = 'Simona'
    password = 'GwvA22c5Sv2l'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('index')
    return redirect('index')


def logout_user(request):
    logout(request)

    return redirect('index')
