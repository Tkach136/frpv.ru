from django.urls import path
from . import views

app_name = 'frpv'

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
    path('test_send/', views.test_send, name='test_send'),
    path('application/', views.application, name='application'),
]
