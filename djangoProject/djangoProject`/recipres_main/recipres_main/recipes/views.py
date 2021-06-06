from django.shortcuts import render, redirect

from recipres_main.recipes.forms import RecipeForm, DeleteRecipeForm
from recipres_main.recipes.models import Recipe


def index(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/index.html', context)


def persist(request, recipe, template_name):
    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipe),
            'recipe': recipe,
        }

        return render(request, f'recipes/{template_name}.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect('home page')

        context = {
            'form': form,
        }
        return render(request, f'recipes/{template_name}.html', context)


def create_recipe_view(request):
    return persist(request, Recipe(), 'create')


def edit_recipe_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return persist(request, recipe, 'edit')


def delete_recipe_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': DeleteRecipeForm(instance=recipe),
            'recipe': recipe,
        }

        return render(request, f'recipes/delete.html', context)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            recipe.save()

        context = {
            'form': form,
        }
        return render(request, f'recipes/details.html', context)


# def delete_recipe_view(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     return persist(request, recipe, 'delete')
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.delete()
    return redirect('home page')


def details_recipe_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'recipes/details.html', context)
