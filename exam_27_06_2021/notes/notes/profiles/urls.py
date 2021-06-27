from django.urls import path

from notes.profiles.views import index_profile, create_profile, delete_profile

urlpatterns = [
    path('', index_profile, name='profile page'),
    path('create/', create_profile, name='create profile'),
    path('delete/', delete_profile, name='delete profile'),
]