from django.urls import path

from pets.views import pet_all_view, pet_detail_view, like_pet_detail_view

urlpatterns = [
    path('', pet_all_view, name='list pets'),
    path('details/<int:pk>/', pet_detail_view, name='pet detail'),
    path('like/<int:pk>/', like_pet_detail_view, name='pet like'),
]