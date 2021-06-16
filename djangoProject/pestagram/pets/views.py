from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from common.forms import CommentForm
from common.models import Comment
from pets.forms import PetCreateForm
from pets.models import Pet, Like


def pet_all_view(request):
    context = {
        'pet': Pet.objects.all(),
    }

    return render(request, 'pets/pet_list.html', context)


def pet_detail_view(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.like_count = pet.like_set.count()

    if request.method == ' GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
        }

        return render(request, 'pets/pet_detail.html', context)
    else:

        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                pet=Pet.objects.get(pk=pk),
                text=form.cleaned_data['comment'],
            )
            # Може и по двата начина
            # comment = Comment(
            #     text=form.cleaned_data['comment'],
            # )
            # pet.comment = comment
            # pet.save()

            return redirect('pet detail', pk)

        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, 'pets/pet_detail.html', context)


def like_pet_detail_view(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()
    return redirect('pet detail', pk)


def create_pet_view(request):
    if request.method == 'GET':

        context = {
            'form': PetCreateForm(),
        }
        return render(request, 'pet_create.html', context)

    else:
        form = PetCreateForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save()
            pet.save()

            return redirect('list pets')

        context = {
            'form': form
        }
        return render(request, 'pet_create.html', context)


def edit_pet_view(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': PetCreateForm(instance=pet)
        }
        return render(request, 'pet_edit.html', context)

    else:
        form = PetCreateForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save()
            pet.save()
            return redirect('list pets')
        context = {
            'form': form
        }
        return render(request, 'pet_edit.html', context)


def delete_pet_view(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.delete()
    return redirect('list pets')
