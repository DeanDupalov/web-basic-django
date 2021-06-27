from django.contrib import admin

# Register your models here.
from notes.note.models import Note

admin.site.register(Note)