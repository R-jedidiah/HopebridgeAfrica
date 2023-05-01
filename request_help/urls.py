from django.urls import path
from .views import help_request

urlpatterns = [
    path('requesthelp/', help_request, name='requesthelp'),
]