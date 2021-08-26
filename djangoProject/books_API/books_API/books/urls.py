from django.urls import path

from books_API.books.views import BookListCreat, BookGetUpdateDelete

urlpatterns = [
    path('', BookListCreat.as_view()),
    path('<int:book_id>', BookGetUpdateDelete.as_view()),
]
