from django.urls import path

from recipres_main.recipes.views import edit_recipe_view, create_recipe_view, index, delete_recipe_view, \
    details_recipe_view, delete_recipe

urlpatterns = [
    path('', index, name='home page'),
    path('create/', create_recipe_view, name='create recipe'),
    path('edit/<int:pk>', edit_recipe_view, name='edit recipe'),
    path('delete/<int:pk>', delete_recipe_view, name='delete recipe'),
    path('submit_delete/<int:pk>', delete_recipe, name='submit delete'),
    path('details/<int:pk>', details_recipe_view, name='details recipe'),
]