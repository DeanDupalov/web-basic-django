from django.shortcuts import render, redirect

# Create your views here.
from pets.models import Pet, Like


def pet_all_view(request):
    context = {
        'pet': Pet.objects.all(),
    }

    return render(request, 'pets/pet_list.html', context)


def pet_detail_view(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.like_count = pet.like_set.count()

    context = {
        'pet': pet,
    }

    return render(request, 'pets/pet_detail.html', context)


def like_pet_detail_view(request, pk):

    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()
    return redirect('pet detail', pk)