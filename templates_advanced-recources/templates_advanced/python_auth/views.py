from django.contrib.auth import logout, authenticate, login
from django.db import transaction
from django.shortcuts import redirect, render

from python_auth.forms import RegisterForm, ProfileForm, LoginForm


@transaction.atomic
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
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
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            return redirect('index')

    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }
    return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)

    return redirect('index')
