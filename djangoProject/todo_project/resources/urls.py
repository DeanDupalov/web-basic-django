from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from resources.views import index_pets, get_private_file

urlpatterns = [
    path('', index_pets, name='index_pets'),
    path('resources/<str:path_to_file>', get_private_file, name='private file')
]
