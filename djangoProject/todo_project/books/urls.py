from django.urls import path

from books.views import index, creat_book_view, edit_book_view, delete_book_view

urlpatterns = [
    path('', index, name='books index'),
    path('create/', creat_book_view, name='creat book'),
    path('edit/<int:pk>', edit_book_view, name='edit book'),
    path('delete/<int:pk>', delete_book_view, name='delete book'),
]
