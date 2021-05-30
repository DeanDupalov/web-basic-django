from django.urls import path

from tasks_todo.views import index, profile_details_view, landing, register, profile_edit_view, profile_delete_view

urlpatterns = [
    path('', landing, name='landing'),
    path('register/', register, name='register'),
    path('list/', index, name='list_profiles'),
    path('details/<int:pk>', profile_details_view, name='profile_details'),
    path('edit/<int:pk>', profile_edit_view, name='profile edit'),
    path('delete/<int:pk>', profile_delete_view, name='profile delete'),
]