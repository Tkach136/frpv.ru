from django.urls import path
from . import views

app_name = 'frpv'

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
    path('application/', views.application, name='application'),
    path('navigator/', views.navigator, name='navigator'),
    path('archive/', views.archive, name='archive'),
    path('news/', views.news, name='news')
]
