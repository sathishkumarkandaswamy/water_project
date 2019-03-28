import django.contrib.auth.views
from django.urls import path
from . import views


urlpatterns = [
   path('water_add/', views.water_add, name='water_add'),
   path('home/', views.index, name='index'),
   path('', views.index, name='index'),
]
