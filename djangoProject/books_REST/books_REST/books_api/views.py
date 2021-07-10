from rest_framework import generics

from books_REST.books_api.models import Book
from books_REST.books_api.serializers import BookSerializer


class BooksListApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):


        return super().perform_update(serializer)