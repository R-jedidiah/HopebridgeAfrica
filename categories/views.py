from django.shortcuts import render, redirect
from categories.models import Category
from categories.models import ChildrenHome
from django.shortcuts import render, get_object_or_404
from .forms import DonorForm



def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})



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

def donor_create(request):
    form = DonorForm()
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form':form
    }
    return render(request, 'categories/donor_create.html', context)





