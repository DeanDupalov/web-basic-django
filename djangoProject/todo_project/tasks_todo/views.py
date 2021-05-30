from django.shortcuts import render
from django.views.decorators.http import require_POST

from tasks_todo.forms import ProfileForm
from tasks_todo.models import Profile


def landing(request):
    return render(request, 'task_todo/landing.html')


def index(request,  form=None):
    if not form:
        form = ProfileForm()
    context = {
        'profiles': Profile.objects.all(),
        'form': form,

    }
    return render(request, 'task_todo/profiles_list.html', context)


def profile_details_view(request, pk):
    profile = Profile.objects.get(pk=pk)

    context = {
        'profile': profile,
    }
    return render(request, 'task_todo/profile_details.html', context)


# @require_POST
def register(request,):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            Profile.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                text=form.cleaned_data['text'],
            )
            form = ProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'task_todo/register.html', context)


def profile_edit_view(request, pk):
    profile = Profile.objects.get(pk=pk)

    form = ProfileForm(initial=profile.__dict__)
    context = {
        'form': form,
    }
    return render(request, 'task_todo/register.html', context)




def profile_delete_view(request, pk):
    pass
