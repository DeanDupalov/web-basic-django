from django.shortcuts import render, redirect

# Create your views here.
from books.forms import BookForm
from books.models import Book


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)


def persist(request, book, template_name):
    if request.method == 'GET':
        context = {
            'form': BookForm(instance=book),
            'book': book,
        }

        return render(request, f'books/{template_name}.html', context)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect('books index')

        context = {
            'form': form,
        }
        return render(request, f'books/{template_name}.html', context)


def creat_book_view(request):
    return persist(request, Book(), 'create')


def edit_book_view(request, pk):
    book = Book.objects.get(pk=pk)
    return persist(request, book, 'edit')


def delete_book_view(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('books index')
