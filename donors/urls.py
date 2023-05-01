from django.urls import path
from . import views
from .views import dashboard
from .views import update_donor
# from .views import delete_donor

# app_name = 'home'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('donor_update/', update_donor, name='donor_update'),
    
]