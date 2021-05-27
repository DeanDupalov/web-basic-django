from django.urls import path

from django301.people.views import index, create_person_view

urlpatterns = [
    path('', index),
    path('create/', create_person_view, name='create person'),
]
