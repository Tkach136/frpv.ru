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
    path('doki/', views.doki, name='doki'),
    path('reliz_proj/', views.reliz_proj, name='reliz_proj'),
    path('proj_razv/', views.proj_razv, name='proj_razv'),
    path('kompl_izd/', views.kompl_izd, name='kompl_izd'),
    path('soglas/', views.soglas, name='soglas'),
]
