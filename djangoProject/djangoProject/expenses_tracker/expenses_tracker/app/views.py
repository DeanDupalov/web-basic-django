from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from core.clean_up import clean_image_files
from core.utiles import get_profile
from expenses_tracker.app.forms import ExpenseForm, ProfileForm, DeleteExpenseForm
from expenses_tracker.app.models import Profile, Expense


def index(request):
    if Profile.objects.exists():
        expenses = Expense.objects.all()
        profile = get_profile()

        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'app/home-with-profile.html', context)
    else:
        return create_profile(request)


def persist(request, expense, template_name):
    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpenseForm(instance=expense),
        }

        return render(request, f'app/{template_name}.html', context)

    else:
        old_image = expense.image
        form = ExpenseForm(request.POST, request.FILES, instance=expense)

        if form.is_valid():
            if old_image:
                clean_image_files(old_image.path)
            form.save()

            return redirect('home page')
        context = {
            'form': form,
        }

        return render(request, f'app/{template_name}.html', context)


def create_expense(request):
    return persist(request, Expense(), 'expense-create')


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    return persist(request, expense, 'expense-edit')


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': DeleteExpenseForm(instance=expense),
        }

        return render(request, f'app/expense-delete.html', context)

    else:
        expense.delete()
        return redirect('home page')


def profile_index(request):
    context = {
        'profile': Profile.objects.first()
    }
    return render(request, 'app/profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(),
        }

        return render(request, 'app/home-no-profile.html', context)

    else:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')

        return render(request, 'app/home-no-profile.html', context={'form': form})


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile)
        }

        return render(request, 'app/profile-edit.html', context)

    else:
        old_image = profile.image

        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            if old_image:
                clean_image_files(old_image.path)
            form.save()

            return redirect('profile page')

        context = {
            'form': form,
        }

        return render(request, 'app/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        context = {
            'profile': profile,
        }

        return render(request, 'app/profile-delete.html', context)
    else:
        old_image = profile.image
        if old_image:
            clean_image_files(old_image.path)
        profile.delete()
        return redirect('home page')
