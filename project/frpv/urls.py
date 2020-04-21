from django.urls import path
from . import views

app_name = 'frpv'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('application/', views.application, name='application'),
    path('navigator/', views.navigator, name='navigator'),
    path('archive/', views.archive, name='archive'),
    path('news/<int:pk>/', views.EntryDetailView.as_view(), name='news'),
    path('about/', views.about, name='about'),
    path('detail/<str:blockname>/', views.navDetail, name='nav_detail'),
    path('struktura/', views.struktura, name='struktura'),
    path('ruko/', views.ruko, name='ruko'),
    path('sovet/', views.sovet, name='sovet'),
    path('expsovet/', views.expsovet, name='expsovet'),
]
