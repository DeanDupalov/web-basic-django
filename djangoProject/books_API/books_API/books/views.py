from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from books_API.books.models import Book
from books_API.books.serializers import BookSerializer


class BookListCreat(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_serializer = BookSerializer(
            data=request.data
        )
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)

        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(APIView):
    def put(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book_serializer = BookSerializer(book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data)

        return Response(book_serializer.errors)

    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book_serializer = BookSerializer(book)
        return Response(book_serializer.data)

    def delete(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)