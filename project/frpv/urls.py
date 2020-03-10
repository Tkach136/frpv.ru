from django.urls import path

from . import views

app_name = 'frpv'

urlpatterns = [
    path('', views.index, name='index'),
]
