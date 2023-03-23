from django.urls import path
from . import views
from .views import categories
from .views import children_home_list
from .views import children_home_details
from .views import donor_create

urlpatterns = [
    path('categories', views.categories, name="categories"),
    path('children_homes/', children_home_list, name='children_home_list'),
    path('children_home_details/<int:pk>/', children_home_details, name='children_home_details'),
    path('add-details/', donor_create),
]