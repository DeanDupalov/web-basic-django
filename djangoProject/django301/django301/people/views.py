from django.shortcuts import render

from django301.models import Person
from django301.people.forms import RawPersonForm


def index(request):
    context = {
        'persons': Person.objects.all()
    }

    return render(request, 'people/index.html', context)


def create_person_view(request):
    my_form = RawPersonForm()

    if request.method == 'POST':
        my_form = RawPersonForm(request.POST)
        if my_form.is_valid():
            Person.objects.create(**my_form.cleaned_data)
            my_form = RawPersonForm()
    context = {
        'form': my_form,
    }
    return render(request, 'people/create_person.html', context)






