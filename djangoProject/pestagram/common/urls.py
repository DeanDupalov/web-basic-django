from django.urls import path

from common.views import landing_page_view

urlpatterns = [
    path('', landing_page_view, name='landing page'),
]