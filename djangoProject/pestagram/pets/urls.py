from django.urls import path


from pets.views import pet_all_view, pet_detail_view, like_pet_detail_view, create_pet_view, edit_pet_view, \
    delete_pet_view

urlpatterns = [
    path('', pet_all_view, name='list pets'),
    path('create/', create_pet_view, name='creat pet'),
    path('edit/<int:pk>', edit_pet_view, name='edit pet'),
    path('delete/<int:pk>', delete_pet_view, name='delete pet'),
    path('details/<int:pk>/', pet_detail_view, name='pet detail'),
    path('like/<int:pk>/', like_pet_detail_view, name='pet like'),
    # path('comment/<int:pk>/', comment_pet, name='comment pet'),
]