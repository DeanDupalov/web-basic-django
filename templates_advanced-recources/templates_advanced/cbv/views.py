from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View, TemplateView

from pythons_app.models import Python

"""
    genetic view
"""


class IndexCbv(View):
    def get(self, request):
        context = {
            'heading_data': 'Hello from View'
        }
        return render(request, 'cbv/index_cbv.html', context)

    def post(self, request):
        pass


"""
    TemplateView
"""


class IndexTemplateView(TemplateView):
    template_name = 'cbv/index_cbv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_data'] = 'Hello from Template View'
        context['pythons'] = Python.objects.all()
        return context

        # return {
        #     'heading_data': 'Hello from Template View',
        #     'pythons': Python.objects.all()
        # }


"""
    ListView
"""


class PythonsListView(ListView):
    template_name = 'cbv/index_cbv.html'
    model = Python
    context_object_name = 'pythons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_data'] = 'List Pythons'

        return context


"""
    DetailView
"""


class PythonsDetailView(DetailView):
    template_name = 'cbv/detail.html'
    model = Python
    context_object_name = 'python'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_data'] = 'Details Python'

        return context


"""
    CreateView
"""


class PythonCreateView(CreateView):
    template_name = 'cbv/create_pet.html'
    model = Python
    fields = '__all__'
    success_url = reverse_lazy('index cbv')
