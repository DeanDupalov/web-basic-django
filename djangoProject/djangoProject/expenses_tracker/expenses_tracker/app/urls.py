from django.urls import path

from expenses_tracker.app.views import index, create_expense, edit_expense, delete_expense, profile_index, edit_profile, \
    delete_profile, create_profile

urlpatterns = [
    path('', index, name='home page'),

    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),

    path('profile/', profile_index, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

]
