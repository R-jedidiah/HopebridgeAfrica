from django.urls import path
from . import views
from .views import categories
from .views import children_home_list
from .views import childrenhome_detail
from .views import donor_create
from .views import ChildrenHome_create
from .views import gallery

urlpatterns = [
    path('categories', categories, name="categories"),
    path('children_homes/', children_home_list, name='children_home_list'),
    path('childrenhome/<int:pk>/', childrenhome_detail, name='childrenhome_detail'),
    path('add-details/', donor_create, name='add-details'),
    path('childrenhome-details/', ChildrenHome_create, name='childrenhome-details'),
    path('childrenhome/<int:pk>/gallery/', gallery, name='gallery'),
]