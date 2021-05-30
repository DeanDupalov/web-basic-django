from django.shortcuts import render
from todo_app.models import Todo
from .forms import TodoForm, RawTodoForm


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todo/index.html', context=context)


# def todo_creat_view(request):
#     form = TodoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = TodoForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'todo/todo_create.html', context)

# def todo_creat_view(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         Todo.objects.create(title=title, description=description)
#     context = {
#
#     }
#     return render(request, 'todo/todo_create_two.html', context)

def todo_creat_view(request):
    my_form = RawTodoForm()

    if request.method == 'POST':
        my_form = RawTodoForm(request.POST)
        if my_form.is_valid():
            Todo.objects.create(**my_form.cleaned_data)
            my_form = RawTodoForm()
    context = {
        'form': my_form
    }
    return render(request, 'todo/todo_create_two.html', context)