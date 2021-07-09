from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from common.forms import CommentForm
from common.models import Comment
from core.clean_up import clean_image_files
from pets.forms import PetCreateForm
from pets.models import Pet, Like


def pet_all_view(request):
    context = {
        'pet': Pet.objects.all(),
    }

    return render(request, 'pets/pet_list.html', context)


@login_required
def pet_details_or_comment_view(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.like_count = pet.like_set.count()

    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
            'can_delete_or_edit': request.user == pet.user.user,
            'can_like': request.user != pet.user.user,
            'has_liked': pet.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != pet.user.user,
        }

        return render(request, 'pets/pet_detail.html', context)

    else:
        form = CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(
                pet=Pet.objects.get(pk=pk),
                text=form.cleaned_data['comment'],
                user=request.user.userprofile,
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


@login_required
def like_pet_detail_view(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        like = Like(user=request.user.userprofile)
        like.pet = pet
        like.save()
    return redirect('pet detail', pk)


@login_required
def create_pet_view(request):
    if request.method == 'GET':
        form = PetCreateForm()
        context = {
            'form': form,
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


@login_required
def edit_pet_view(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': PetCreateForm(instance=pet)
        }
        return render(request, 'pet_edit.html', context)

    else:
        old_image = pet.image
        form = PetCreateForm(request.POST, request.FILES, instance=pet)

        if form.is_valid():
            if old_image:
                clean_image_files(old_image.path)
            pet = form.save()
            pet.save()
            return redirect('list pets')
        context = {
            'form': form
        }
        return render(request, 'pet_edit.html', context)


@login_required
def delete_pet_view(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':

        context = {
            'pet': pet,
        }
        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')
