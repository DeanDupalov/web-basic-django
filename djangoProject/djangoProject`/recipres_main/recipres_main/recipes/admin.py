from django.contrib import admin

# Register your models here.
from recipres_main.recipes.models import Recipe

admin.site.register(Recipe)