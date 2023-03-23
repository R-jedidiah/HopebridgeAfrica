from django.urls import path
from . import views

# app_name = 'home'
urlpatterns = [
    path('', views.base_home, name=''),
    path('home', views.home, name="home"),
]