from django.shortcuts import render, redirect

# Create your views here.
from core.utils import get_profile, get_notes_count
from notes.note.models import Note
from notes.profiles.forms import ProfileForm


def index_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
        'notes_count': get_notes_count()
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if profile:
        profile.delete()
        Note.objects.all().delete()
        return redirect('home page')
    return redirect('home page')


