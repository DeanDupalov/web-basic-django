from django.contrib import admin

# Register your models here.
from notes.profiles.models import Profile

admin.site.register(Profile)