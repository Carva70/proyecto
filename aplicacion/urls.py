from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('usuario', views.index, name='index'),
    path('', RedirectView.as_view(url='usuario', permanent=True), name='default')
]