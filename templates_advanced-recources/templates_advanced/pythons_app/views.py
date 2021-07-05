from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from core.mixins.group_required_mixin import GroupRequiredMixin
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
# def index(request):
#     pythons = Python.objects.all()
#     """
#         Добавихем функционалност само потребителя който е добавил питона да може да го изтрива!
#         Тук и в темплейта
#     """
#     # for python in pythons:
#     #     python.can_delete = python.created_by_id == request.user.id
#     return render(request, 'index.html', {'pythons': pythons})

class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'


# def create(req):
#     if req.method == 'GET':
#         form = PythonCreateForm()
#         return render(req, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(req.POST, req.FILES)
#
#         if form.is_valid():
#             python = form.save()
#             python.save()
#             return redirect('index')

class CreatePythonView(GroupRequiredMixin, FormView):
    template_name = 'create.html'
    form_class = PythonCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    group_required = ['User']
