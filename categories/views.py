from django.shortcuts import render
from categories.models import Category
from categories.models import ChildrenHome
from django.shortcuts import render, get_object_or_404
from .models import ChildrenHomeDetails


def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})

from django.shortcuts import render
from .models import ChildrenHome

def children_home_list(request):
    county = request.GET.get('county')
    children_homes = ChildrenHome.objects.all()
    if county:
        children_homes = children_homes.filter(county=county)
    context = {
        'children_homes': children_homes
    }
    return render(request, 'categories/children_home_list.html', context)

def children_home_details(request, pk):
    home = get_object_or_404(ChildrenHome, pk=pk)
    return render(request, 'children_home_details.html', {'children_home_details.html': children_home_details})






