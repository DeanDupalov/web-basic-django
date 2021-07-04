from django.urls import path

from cbv.views import IndexCbv, IndexTemplateView, PythonsListView, PythonsDetailView, PythonCreateView

urlpatterns = [
    path('', IndexCbv.as_view(), name='index cbv'),
    path('2/', IndexTemplateView.as_view(), name='index cbv 2'),
    path('list/', PythonsListView.as_view(), name='cbv python list'),
    path('detail/<int:pk>', PythonsDetailView.as_view(), name='cbv python detail'),
    path('create/', PythonCreateView.as_view(), name='cbv python create'),
]
