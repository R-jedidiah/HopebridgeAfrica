from django.urls import path
from . import views

urlpatterns = [
    path('registration/signin', views.signin, name="signin"),
    path('registration/signup', views.register,  name="signup"),
    
    
    
]