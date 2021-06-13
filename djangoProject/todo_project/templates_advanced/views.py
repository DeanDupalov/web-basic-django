from django.shortcuts import render

# Create your views here.
from templates_advanced.forms import ItemFrom
from templates_advanced.models import Item


def index(request):
    context = {
        'items': Item.objects.all(),
        'form': ItemFrom,
    }
    return render(request, 'templates_advanced/index.html', context)
