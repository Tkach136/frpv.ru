from django.urls import path

from . import views

app_name = 'frpv'

urlpatterns = [
    path('', views.index, name='index'),
    path('application/send', views.send, name='send'),
    path('application', views.application, name='application'),
]
