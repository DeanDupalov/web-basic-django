from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('auth/', include('python_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
