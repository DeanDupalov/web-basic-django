from os.path import join, isfile

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from resources.forms import PetForm
from resources.models import Pet


def index_pets(request):
    if request.method == 'GET':
        context = {
            'pets': Pet.objects.all(),
            'form': PetForm(),
        }

        return render(request, 'pets/index_pets.html', context)

    else:
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save()
            pet.save()
            return redirect('index_pets')

        context = {
            'pets': Pet.objects.all(),
            'form': form,
        }
        return render(request, 'pets/index_pets.html', context)


def get_private_file(request, path_to_file):
    full_path = join(settings.MEDIA_ROOT, 'private', path_to_file)
    if isfile(full_path):
        file = open(full_path, 'rb')
        response = HttpResponse(content=file)
        response['Content-Disposition'] = 'attachment'
        return response
    return None
