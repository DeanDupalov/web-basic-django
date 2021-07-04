from django.shortcuts import render, redirect

from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(request):
    pythons = Python.objects.all()
    """
        Добавихем функционалност само потребителя който е добавил питона да може да го изтрива!
        Тук и в темплейта
    """
    for python in pythons:
        python.can_delete = python.created_by_id == request.user.id
    return render(request, 'index.html', {'pythons': pythons})


def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(req.POST, req.FILES)

        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
